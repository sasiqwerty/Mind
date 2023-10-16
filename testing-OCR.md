---
aliases: 
tags: 
date created: Monday, October 16th 2023, 11:17:49 am
date modified: Monday, October 16th 2023, 11:32:58 am
---

## Code

```python
import cv2

import pytesseract

import os

  

def preprocess_image(image):

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return threshold_image

  

# Create the 'text' directory if it doesn't exist

if not os.path.exists('text'):

    os.makedirs('text')

  

# Open a single text file to store all the OCR results

with open('text/all_text_output.txt', 'w') as output_file:

    # Loop through all the files in the 'images' directory

    for filename in os.listdir('images'):

        try:

            if filename.endswith('.jpg') or filename.endswith('.png'):  # Filter image files

                img_path = os.path.join('images', filename)

                img = cv2.imread(img_path)

  

                if img is None:

                    raise FileNotFoundError(f"Image {filename} not found")

                processed_img = preprocess_image(img)

                text = pytesseract.image_to_string(processed_img)

                if not text:

                    raise ValueError(f"No text found in the image {filename}")

  

                # Write the image name as a heading and its OCR text into the single text file

                output_file.write(f"{filename}\n")

                output_file.write(f"{text}\n\n")

                print(f"Processed {filename} and appended the text to all_text_output.txt")

  

        except FileNotFoundError as fnf_error:

            print(fnf_error)

        except ValueError as ve:

            print(ve)

  

        except Exception as e:

            print(f"An unexpected error occurred: {e}")
```

## Output

`[Running] python -u "c:\Users\sarat\OneDrive\Desktop\folders\dump-test\test.py"`  
WhatsApp Image 2023-10-15 at 11.01.27_14ffa2af.jpg  
Your organization has a requirement to allow only one user to “check out passwords” and connect through the PSM securely.  
What needs to be configured in the Master policy to ensure this will happen?

OA Enforce check-in'check-out exclusive access = active, Require privileged session monitor ng and isolation = active

0B. Enforce check-in‘check-out exclusive access =

mactive: Require privileged session monitoring and isolation = inactive

OC. Enforce check-inicheck-out exclusive access = inactive, Record and save session activity = active

oD. Enforce check-in/check-out exclusive access = active, Record and save session activity = active



WhatsApp Image 2023-10-15 at 11.01.27_5bf82ef3.jpg  
The Privileged Access Management solution provides an out-of-the-box target platform to manage SSH keys. called UNIX Via SSH Keys.  
” How are these keys managed?

OA CyberArk stores Private keys in the Vault and updates Public keys on target systems

QB CyberArk stores Public keys in the Vault and updates Private keys on target systems

EOC, CyberArk does not store Public or Private keys and instead uses a reconcile account to create keys on demand

OD. CyberArk stores both Private and Public keys and can update target systems with either key



WhatsApp Image 2023-10-15 at 11.01.27_ea51b6cf.jpg  
What can you do to ensure each com

xe) A.  
© B.  
“OC

OD

PONEAL Sever Ss operat onal?

Logon to PVWA with v1 Ui navigat

eto Heath,

4 and validate earch ¢ omponent serv.

$ Conner  
Ping each component server to

StS

Use the PrivateArk cient to cor

‘ver_and vaildale all the services are fun

mwnAg  
Install the Vault Server interface one

femote maci

ne tC avond interactive logan to the Vauit OS and review the ITAL

rough the Vault Server interface



WhatsApp Image 2023-10-15 at 11.01.28_9d7b7b19.jpg  
CyberArk Defender - PAM - Dattatraya B Ingale

What must you specify when contouring a dist overy Seat for NIK?! (sanse 21

tA Vault Adminstuaty  
B CPM Scanbe:  
me foot password for ean h machine  
tL! D hst of machines to scan

CLE safe for discovered accounts



WhatsApp Image 2023-10-15 at 11.01.28_aeb1356e.jpg  
yberArk Defender - PAM - Dattatraya B Ingale

According to CyberArk, which issues most commonly cause Installed components to display 4 discorinected in the System Health Dashboard? (Choose 2

Qa network instabiities:outages

QB vault license expiry  
oc credential de-sync  
ao browser compatibility issues

| O E. installed location file corruption



WhatsApp Image 2023-10-15 at 11.01.28_d6d6e70f.jpg  
COR  
OB.  
boc  
=O D.

List Accounts. Use Accounts  
List Accounts. Use Accounts  
Use Accounts

List Accounts. Use Accounts

E. To use PSM connections while in the PVWA what are the minimum safe permissions a user or group will need?

Retrieve Accounts

Retrieve Accounts, Access Safe without confirmation