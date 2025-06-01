import os
from archiveUtil import ArchiveUtil
from myList import MyList
import datetime
import random
# -*- coding: utf-8 -*-
def test_binary_file_processing_with_mylist():
    #buscador directorio
    storage_path = os.path.join('src', 'Storage')
    
    os.makedirs(storage_path, exist_ok=True)
    #define el formato del nombre de archivo
    binary_file_name = "random_representation_numbers.bin"
    
    actualDateTime = datetime.datetime.now()
    formattedDateTime = actualDateTime.strftime("%Y-%m-%d_%H-%M-%S")
    rand = random.randint(1, 100)

    output_text_file_name = f"extracted_numbers{formattedDateTime}_serial{rand}"

    # Initialize MyList instead of a standard Python list
    extracted_strings_my_list = MyList()
    try:
        archive_util = ArchiveUtil(storage_path)

        print(f"Lectura de archivo binario: {binary_file_name}")
        binary_archive_stream = archive_util.get_archive(binary_file_name)
        
        binary_content = binary_archive_stream.read()
        binary_archive_stream.close()
        
        decoded_content = binary_content.decode('utf-8')
        
        # Extract each string separated by '#' and add it to MyList
        for s in decoded_content.split('#'):
            if s: # Only add non-empty strings
                extracted_strings_my_list.append(s)

        print("\nExtracted strings stored in MyList:")
        # You can iterate over MyList directly
        for item in extracted_strings_my_list:
            print(f"- {item}")
        
        # Or print the entire MyList object
        print(f"\nMyList object content: {extracted_strings_my_list}")
        print(f"Number of items in MyList: {len(extracted_strings_my_list)}")

        # --- Optional: Write the contents of the list to a text file ---
        # Convert MyList to a standard Python list for easy joining
        if len(extracted_strings_my_list) > 0:
            content_to_write = "\n".join(extracted_strings_my_list.to_list())
            
            full_output_path = os.path.join(storage_path, f"{output_text_file_name}.txt")
            with open(full_output_path, 'w') as file:
                file.write(content_to_write)
            
            print(f"\nAll extracted strings written to '{output_text_file_name}.txt' in {storage_path}")
        else:
            print("\nNo strings extracted to write to file.")

        # Optional: Verify the content of the created text file
        if os.path.exists(full_output_path):
            with open(full_output_path, 'r') as f:
                verified_content = f.read()
            print(f"\nContent of {output_text_file_name}.txt:\n{verified_content}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        pass

if __name__ == "__main__":
    test_binary_file_processing_with_mylist()