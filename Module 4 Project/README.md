# Project Problem Statement
Okay, here's the scenario:

You work for an online fruit store, and you need to develop a system that will update the catalog information with data provided by your suppliers. When each supplier has new products for your store, they give you an image and a description of each product.

Given a bunch of images and descriptions of each of the new products, you’ll:

- Upload the new products to your online store. Images and descriptions should be uploaded separately, using two different web endpoints.

- Send a report back to the supplier, letting them know what you imported.

Since this process is key to your business's success, you need to make sure that it keeps running! So, you’ll also:

- Run a script on your web server to monitor system health.

- Send an email with an alert if the server is ever unhealthy.

Hopefully this summary has helped you start thinking about how you’ll approach this task. In case you’re feeling a little scared, don't worry, you can definitely do this! You have all the necessary tools, and the lab description will go into a lot more detail of what you need to do.

Up next, we'll give you a few tips that can help you along the way.

## Fetching supplier data
You'll first need to get the information from the supplier that is currently stored in a Google Drive file. The supplier has sent data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description).

Here, you'll find two script files download_drive_file.sh and the example_upload.py files. You can view it by using the following command.

