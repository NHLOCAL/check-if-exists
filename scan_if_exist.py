import os
import sys
# יבוא פונקציה לקריאת עץ תיקיות
from os.path import join, getsize

def scan_if_exist(file_to_scan, files_list):
    """
    הפונקציה בודקת קובץ יחיד האם הוא קיים בעץ תיקיות היעד   
    """
    if file_to_scan in files_list:
        return True
    else:
        return False


def main(dir_to_scan, target_dir):
    """
    הפונקציה עוברת על רשימת קבצים בתיקית המקור
    ומפעילה עליהם את פונקציית "scan_if_exist"
    
    פרמטרים:
    פרמטר 1 = נתיב תיקיה המכילה רשימת קבצים להעתקה
    פרמטר 2 = נתיב תיקית יעד
    """
    # קריאת האינדקס מתוך קובץ מוכן
    index_file = "index-files.txt"
    if os.path.exists(index_file):
        with open(index_file, 'r') as f:
            files_list = [line.strip() for line in f]
        print(files_list)
    else:
    # יצירת רשימת הקבצים הקיימים בעץ התיקיות
        files_list = []
        for root, dirs, files in os.walk(target_dir):
            if files != []:
                files_list += files
        # הכנסת הרשימה המוכנה לקובץ
        with open(index_file, 'w') as f:
            for item in files_list:
                f.write(str(item) + '\n')
    
    # הגדרת רשימת הקבצים בתיקיה
    list_dir = os.listdir(dir_to_scan)
    

    
    # מעבר על רשימת הקבצים בתיקית המקור והפעלת פונקציית "scan_if_exist"    
    for file_to_scan in list_dir:
        answer = scan_if_exist(file_to_scan, files_list)
        if answer:
            print('"{}" {}'.format(file_to_scan, "exist file!"))    


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
