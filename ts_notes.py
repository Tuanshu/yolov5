# python detect.py --source C:\Users\TuanShu\repos\yolov5\l_light_01_missing_hole_01_1_600.jpg --weight C:\Users\TuanShu\repos\yolov5\ts\best.pt
# python detect.py --source \l_light_01_missing_hole_01_1_600.jpg --weight \ts_public\best.pt
# l_light_04_missing_hole_01_5_600

# python detect.py --source C:\Users\TuanShu\repos\yolov5\l_light_04_missing_hole_01_5_600.jpg --weight C:\Users\TuanShu\repos\yolov5\ts_public\best.pt

from detect import main, parse_opt
import os
root_folder_path = 'C:/Users/TuanShu/repos/yolov5/'
source_file_path_rel = 'l_light_04_missing_hole_01_5_600.jpg'
weight_path_rel = 'ts_public/best.pt'


source_file_path = os.path.join(root_folder_path, source_file_path_rel)
weight_path = os.path.join(root_folder_path, weight_path_rel)

opt = parse_opt()
opt.weights = weight_path
opt.source = source_file_path

print(weight_path)
main(opt)
