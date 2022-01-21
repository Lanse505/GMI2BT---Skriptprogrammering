from util import project_json as json
from util import project_csv as csv
from util import project_validation as validation

if __name__ == "__main__":
    target_csv = input("Please enter the path for your targetted csv: ")
    while not validation.validate_file_path(target_csv):
        print("Error: Invalid File Path, Make sure to provide a valid filepath to your csv!")
        target_csv = input("Please enter the path for your targetted csv: ")
    csv_reader = csv.openCSVFile(target_csv, 'r+')
    temp_json = json.openJSONFile("/temp.json" 'r+')

    


