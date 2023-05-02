from tkinter import *
import boto3
import os
import sys
from tempfile import gettempdir
from contextlib import closing


root=Tk()
root.geometry("500x500")
root.title("speechify")

text_bar= Text(root,height=10)
text_bar.pack()

def inputText():
    aws_mag_con=boto3.session.Session(profile_name='suhail7412')
    client=aws_mag_con.client(service_name='polly',region_name='ap-southeast-2')
    ans= text_bar.get("1.0","end")
    print(ans)
    response=client.synthesize_speech(VoiceId='Joanna',OutputFormat='mp3',text=ans,Engine='neural')
    print(response)
    if "AudioStream" in response:
        with closing(response['AudioStream']) as stream:
            output=os.path.join(gettempdir(),"speech.mp3")
            try:
                with open(output,"wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)
    else:
        print("could not find the stream....")
        sys.exit(-1)
    if sys.platform=='win32':
        os.startfile(output)


show=Button(root,height=1,width=10,text="Read",command=inputText)
show.pack()


root.mainloop()