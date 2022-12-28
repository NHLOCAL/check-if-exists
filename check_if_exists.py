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


def main(dir_to_scan, target_dir, index=None):
    """
    הפונקציה עוברת על רשימת קבצים בתיקית המקור
    ומפעילה עליהם את פונקציית "scan_if_exist"
    
    פרמטרים:
    פרמטר 1 = נתיב תיקיה המכילה רשימת קבצים להעתקה
    פרמטר 2 = נתיב תיקית יעד
    פרמטר 3 = אופציונלי "True" או "False". ברירת המחדל היא "None"
    """
    # הגדרת משתנה עבור נתיב קובץ אינדקס מותאם לתיקית היעד
    index_file = os.path.join(target_dir,"index-files.txt")
    
    # קריאה מתוך קובץ, אם ישנו ואם לא הוגדרה בנייה מחדש של האינדקס
    if os.path.isfile(index_file) and not index:
        with open(index_file, 'r') as f:
            files_list = [str(line.strip()) for line in f]
   
    # יצירת רשימת הקבצים הקיימים בעץ התיקיות   
    else:
        files_list = []
        for root, dirs, files in os.walk(target_dir):
            if files != []:
                files_list += files

        # הכנסת הרשימה לקובץ, אם לא הוגדר במפורש שלא לבנות אינדקס             
        if index != False:
            # ביטול הסתרת קובץ האינדקס לצורך כתיבה עליו
            if os.path.isfile(index_file): os.system('attrib -s -h ' + index_file)
            with open(index_file, 'w') as f:
                for item in files_list:
                    try: f.write(str(item) + '\n')
                    except: pass
            # הסתרת קובץ האינדקס
            os.system('attrib +s +h ' + index_file)
                    
    
    # הגדרת רשימת הקבצים בתיקיה
    list_dir = os.listdir(dir_to_scan)
   
    # מעבר על רשימת הקבצים בתיקית המקור והפעלת פונקציית "scan_if_exist"    
    for file_to_scan in list_dir:
        answer = scan_if_exist(file_to_scan, files_list)
        if answer:
            print('"{}" {}'.format(file_to_scan, "exist file!"))    


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], index=eval(sys.argv[3]))
