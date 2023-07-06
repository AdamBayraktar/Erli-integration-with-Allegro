# simply text file convertor into list
# each id must start from new line

def main():
    the_list = convert_text_file_to_list("list_of_product_id.txt")
    for item in the_list:
        print(item)

def convert_text_file_to_list(file):
    with open(file, "r") as f:
        id_list = f.readlines()       
        # strip new line add the end of id
        id_list = [id.strip("\n") for id in id_list]
        return id_list
    
    
if __name__ == "__main__":
    main()