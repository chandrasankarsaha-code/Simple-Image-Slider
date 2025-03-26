import tkinter
from tkinter import *
# Importing necessary modules for handling images
from PIL import ImageTk, Image

# Initialize the main application window
root=Tk()
root.title("Image Slider") # Set the title of the window
root.geometry("300x250") # Set the size of the window


# Function to load and resize images
def load_image(path, width, height):
    img = Image.open(path)
    img = img.resize((width, height), Image.LANCZOS)  # Resize to fit the window
    return ImageTk.PhotoImage(img) # Convert the image to a format compatible with Tkinter


# Load resized images
img1 = load_image("img1.png", 300, 200)
img2 = load_image("img2.png", 300, 200)
img3 = load_image("img3.png", 300, 200)
img4 = load_image("img4.png", 300, 200)
img5 = load_image("img5.png", 300, 200)
img6 = load_image("img6.png", 300, 200)

# List to store all images for easy navigation
img_list = [img1, img2, img3, img4, img5, img6]

# Display the first image in the slider
img=Label(image=img1)
img.grid(row=0,column=0,columnspan=3,)

# Label to show current image number
img_no=Label(root,text=f" 1 of {len(img_list)}")
img_no.grid(row=2,column=2,)


# Function to move forward in the image list
def forward(image_number):
    global img,button_forward,button_back

    img.grid_forget() # Remove the current image
    img=Label(image=img_list[image_number-1]) # Load the next image

    # Create navigation buttons
    button_forward =Button(root,text='>>',command=lambda:forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda:back(image_number-1))
    
    # Disable the forward button if the last image is reached
    if image_number==6:
        button_forward=Button(root,text=">>",state=DISABLED)
    
    # Display the updated image and buttons
    img.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
     
    # Update the image number display
    img_no.config(text=f"{image_number} of {len(img_list)}")


# Function to move backward in the image list
def back(image_number):
    global img,button_forward,button_back

    img.grid_forget() # Remove the current image
    img=Label(image=img_list[image_number-1]) # Load the previous image

     # Create navigation buttons
    button_forward =Button(root,text='>>',command=lambda:forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda:back(image_number-1))
    
    # Disable the back button if the first image is reached
    if image_number==1:
        button_back=Button(root,text="<<",state=DISABLED)
    
    # Display the updated image and buttons
    img.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    # Update the image number display
    img_no.config(text=f"{image_number} of {len(img_list)}")

# Create and position the initial buttons
button_forward=Button(root,text=">>",command=lambda:forward(2))
button_forward.grid(row=1,column=2)

# Exit button
exitbtn=Button(root,text="Exit",command=root.quit) 
exitbtn.grid(row=1,column=1)

# Initially disabled back button
button_back=Button(root,text="<<",command=back,state=DISABLED)
button_back.grid(row=1,column=0)


# Start the Tkinter event loop
root.mainloop()