# Sources I used:
# https://docs.python.org/3/library/xml.etree.elementtree.html     - ElementTree
# https://peps.python.org/pep-0008/#comments                       - Convention (PEP - Comments)
# Google                                                           - Misc stuff such as looking up For loop, Try Catch, Docs etc...

# Import Libraries
import xml.etree.ElementTree as ET


# Run XML File Method
def run_xml_file(file, id):
    try:
        # Parse the XML file
        tree = ET.parse(file)
        root = tree.getroot()

        # Loop through each element in the XML file
        for child in root.iter():
            # Check if id attribute matches the required id when calling function/method
            if child.get('id') == id:
                # If target is found it will print the element 'target's text (string)
                target = child.find('target').text
                if target is not None:
                    print(f"Element id: {id}, Target: {target}")
                else:
                    print(f"Element with id {id} does not have a 'target' attribute.")

        return target

    except FileNotFoundError:
        print('Exception Occured, File not found, please write the correct filename in order to run the method.')
    except ET.ParseError:
        print('Exception Occured, Could not Parse.')


# Save value to file (.txt)
def save_value_to_file(file ,value, outputfile):
    # If file does not exist, opens 'target.txt' and writes to file
    with open(outputfile, 'w') as f:
        # Runs 'run_xml_file' to receive the value of 'target' of required value/id and writes a line of 'target' to file
        f.writelines(run_xml_file(file, value))
        print('----------------------------------')
        print(f'Value/id: {value} from file: {file} saved to file: {outputfile}')
        print('----------------------------------')


# Run Program
if __name__ == '__main__':
    # Parses the XML file and prints the id and target.
    #run_xml_file('sma_gentext.xml', '42007')

    # Runs 'run_xml_file' and returns the target from required value and saves it to a .txt file
    save_value_to_file('sma_gentext.xml', '42007', 'target.txt')

    # Will Not Work
    run_xml_file('', '')
