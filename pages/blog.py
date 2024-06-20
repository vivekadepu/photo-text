import streamlit as st
st.title("Turn your photos into notes with AI")
st.write("The project aims to quickly convert your photos in to  description to the markdown notion editable text format by uploading an image on drop down")
st.image("https://raw.githubusercontent.com/vivekadepu/photo-text/main/image1.jpg")

st.write("The main interface of the app is designed to be user-friendly and easy to use")





st.subheader('Key Features of the App')
st.image("https://raw.githubusercontent.com/vivekadepu/photo-text/main/image2.jpg", caption="QR Code Scanner", width=250)

st.markdown(


"""

1. **QR Code Scanner**: 
   - The app provides a QR code for easy access.By Simply scanning the QR Code we can directly open the app in the url. 
   - The QR code is located on the left side of the interface for quick and convenient access.
2. **Obsidian DB Path**:
   - On the left side, below the QR code, there's an input box for specifying the path to your Obsidian database. 
   - Obsidian allows users to organize their notes in a folder structure.We can directly access the path to the folder.
   - This feature ensures that your notes can be directly integrated into your Obsidian workspace for seamless note-taking.
3. **Model Selection**:
   - The app includes a dropdown menu to select the AI model for text extraction. 
   - Currently, the "gpt-4o" model is available, with more options to be added in future updates.  
4. **OCR Enhance Option**:
   - For enhanced text extraction, there's a checkbox option to use OCR enhancement.
   - OCR(Optical Character Recognition) 
   - Enabling this feature improves the accuracy of text extraction from images.  


"""
)



st.image("https://raw.githubusercontent.com/vivekadepu/photo-text/main/image3.jpg", caption="Note Title Input",width=600)

st.markdown(

"""


1. **Note Title Input**:
   - At the top center of the APP interface, you will find a text box labeled "Note Title".
   - Here, you can input the title of your note what you want .you can organize your extracted text effectively.
   - It is used mainly for giving title to your note.

2. **File Upload In (Your Photos)**:
   - The app allows you to upload your photos for text extraction. 
   - The file uploader supports drag-and-drop functionality and accepts files up to 200MB in size. 
   - It Supports file types include `.jpg`, `.jpeg`, and `.jpg` formats
   - Uploaded files are displayed with their names and sizes for easy identification.
   - It take very less time period for upload and extract the data from the image.

"""
)

st.image("https://raw.githubusercontent.com/vivekadepu/photo-text/main/image4.jpg", caption="sample image uploading for testing",width=300)


st.subheader("Result")

st.image("https://raw.githubusercontent.com/vivekadepu/photo-text/main/image5.jpg", caption="output of the above sample image",use_column_width=True)

st.markdown(

"""


1. **Output**:

   ### Commentary on AI and Daily Chores
   
   - The quote emphasizes the desire for AI to handle mundane tasks to free up time for creative activities.

   - "I want AI to do my laundry and dishes so that I can do art and writing, not for AI to do my art and writing so that I can do my laundry and dishes."

   - Author and video game enthusiast Joanna Maciejewska highlights the importance of AI aiding in daily chores to prioritize creative pursuits.
   - *(Note: Although bathroom cleaning goes ahead of laundry and dishes)*)*

2. **Done**:

   - Hence result has been showed in a above extracted text format.

"""
)   

st.subheader("How it works")

st.markdown(

"""

###Steps to use the apps

1. **Upload an Image**: 
   - Click on the "Browse files" button or drag and drop file here and choose your file Supports file types include `.jpg`, `.jpeg`, and `.jpg` formats up to 200MB size.
   - It's take very less time.

2. **Taking Notes**:
   - Once an image is uploaded, the app processes the image and extracts text using the selected AI model.
   - A loading indicator shows the progress with a "Taking notes..." message.

3. **Review and Edit**:
   - The extracted text is displayed in a text area where you can review and edit your notes before saving or exporting them.

"""
)

st.subheader("Conclusion")

st.markdown(

"""
 - This app uses AI to convert handwritten notes, printed documents, or any text in images into digital notes. 
 - Start by scanning the QR code or uploading an image to see the benefits of AI note-taking.
 - It is very useful one for upcoming technology.

"""
)
