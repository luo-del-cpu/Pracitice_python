import os
import json
import numpy as np

IOU_THRESHOLD = 0.5

def compute_iou(box1, box2):
    xA = max(box1[0], box2[0])
    yA = max(box1[1], box2[1])
    xB = min(box1[2], box2[2])
    yB = min(box1[3], box2[3])
    interArea = max(0, xB - xA) * max(0, yB - yA)
    box1Area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2Area = (box2[2] - box2[0]) * (box2[3] - box2[1])
    iou = interArea / float(box1Area + box2Area - interArea + 1e-6)
    return iou

def evaluate_one_patient(gt_file, pred_file):
    with open(gt_file) as f:
        gt_data = json.load(f)
    with open(pred_file) as f:
        pred_data = json.load(f)

    gt_dict = {item["image"]: item["gt_boxes"] for item in gt_data["slices"]}
    pred_dict = {item["image"]: item["pred_boxes"] for item in pred_data["slices"]}

    TP, FP, FN, total_iou = 0, 0, 0, []

    for img_name in gt_dict:
        gt_boxes = gt_dict.get(img_name, [])
        pred_boxes = pred_dict.get(img_name, [])
        matched = set()

        for p_box in pred_boxes:
            found_match = False
            for i, g_box in enumerate(gt_boxes):
                iou = compute_iou(p_box, g_box)
                if iou >= IOU_THRESHOLD and i not in matched:
                    TP += 1
                    total_iou.append(iou)
                    matched.add(i)
                    found_match = True
                    break
            if not found_match:
                FP += 1

        FN += len(gt_boxes) - len(matched)

    precision = TP / (TP + FP + 1e-6)
    recall = TP / (TP + FN + 1e-6)
    f1 = 2 * precision * recall / (precision + recall + 1e-6)
    avg_iou = np.mean(total_iou) if total_iou else 0.0

    return {
        "patient_id": gt_data["patient_id"],
        "TP": TP, "FP": FP, "FN": FN,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "avg_iou": avg_iou
    }

def evaluate_all_patients(data_root):
    results = []
    fp_patients = []
    fn_patients = []

    for patient_id in os.listdir(data_root):
        path = os.path.join(data_root, patient_id)
        gt_file = os.path.join(path, "gt.json")
        pred_file = os.path.join(path, "pred.json")
        if os.path.exists(gt_file) and os.path.exists(pred_file):
            result = evaluate_one_patient(gt_file, pred_file)
            results.append(result)
            print(f"{result['patient_id']}\tP={result['precision']:.3f}\tR={result['recall']:.3f}\tF1={result['f1']:.3f}\tIOU={result['avg_iou']:.3f}")
            if result["FP"] > 0:
                fp_patients.append(result["patient_id"])
            if result["FN"] > 0:
                fn_patients.append(result["patient_id"])

    # 总体指标
    total_tp = sum(r["TP"] for r in results)
    total_fp = sum(r["FP"] for r in results)
    total_fn = sum(r["FN"] for r in results)
    total_iou_list = sum([r["avg_iou"] * r["TP"] for r in results], 0.0)
    total_iou_count = sum(r["TP"] for r in results)

    precision = total_tp / (total_tp + total_fp + 1e-6)
    recall = total_tp / (total_tp + total_fn + 1e-6)
    f1 = 2 * precision * recall / (precision + recall + 1e-6)
    avg_iou = total_iou_list / (total_iou_count + 1e-6)

    print("\n📊 全部病例汇总")
    print(f"✔ Total TP: {total_tp}")
    print(f"❌ Total FP: {total_fp}")
    print(f"⚠ Total FN: {total_fn}")
    print(f"📈 Precision: {precision:.4f}")
    print(f"📉 Recall:    {recall:.4f}")
    print(f"🎯 F1-score:  {f1:.4f}")
    print(f"📏 Avg IOU:   {avg_iou:.4f}")

    print("\n📌 有误报的病例：")
    for pid in fp_patients:
        print(f" - {pid}")

    print("\n📌 有漏检的病例：")
    for pid in fn_patients:
        print(f" - {pid}")

# 示例：调用
# evaluate_all_patients("data")
