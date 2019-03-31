from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = """Dealing With Trauma After A Mass Shooting — Over The Long Term

By Scott Simon

NPR.org, March 30, 2019 · Fresh waves of grief have hit the communities of Parkland, Fla., and Newtown, Conn., after recent news of more deaths.

On Monday, the father of a girl who was killed in the 2012 Sandy Hook Elementary School shooting died by apparent suicide, and last week, two students who survived the Marjory Stoneman Douglas High School shooting took their own lives.

It's impossible to know the exact reason these people decided to take their lives, but their heartbreaking deaths have sparked conversation about how to support people after unthinkable tragedies, especially over the long term.

It took Sherrie Lawson a long time to stop having daily panic attacks.

Lawson, now 45, was inside the Washington Navy Yard when a gunman shot 12 people dead and injured three others on Sept. 16, 2013. She escaped by scaling an 8-foot brick wall. She knew three of the victims personally.

"In the immediate aftermath of the shooting, I was in shock. I was confused," she told NPR's Scott Simon. "It took a lot of time to process what was going on. But after about a month or so, my symptoms actually became worse."

She wasn't sleeping. She was having nightmares almost daily, as well as panic attacks. It was hard for her to focus. On normal visits to the grocery store, Lawson found herself constantly scanning her surroundings for possible danger and checking for escape exits.

"Going into grocery stores was really difficult for me because I couldn't see over the rows of food," she said.

This reminded her of building 197, where the Washington Navy Yard shooting took place, because building 197 was a cube farm.

"It was just rows and rows of cubes and it was a maze," she said.

The similarities were enough to trigger panic attacks for Lawson. She said she's had panic attacks the in the middle of the grocery store and in comparable environments like Target.

"After probably the third month of experiencing this, I realized that I was not OK and that I needed some help. So I did seek out a doctor," she said.

Once she got professional medical help, Lawson was officially diagnosed with post-traumatic stress disorder (PTSD), major depressive disorder and severe anxiety. She also struggled with suicidal thoughts.

"I felt like this was gonna be my life forever," she said. "I didn't see it getting better and I just I didn't want to live like that."

Because of the level of stress she was experiencing, Lawson started to experience heart issues. About one year after the shooting, she suffered a mini-stroke because her right carotid artery burst spontaneously and she was hospitalized. The burst artery was attributed to her high stress levels.

After that, Lawson decided to put her health first — she dropped out of work and school. At the time of the shooting, she was a doctoral candidate working on her dissertation.

"I did have to come out of that program and pretty much drop all of the major responsibilities that I had had in my life at that point and focus solely on my health and just trying to get better," she said.

Her doctor entered her into a PTSD trauma intensive program, which put her in numerous types of therapy almost every day from 9 a.m. to 3 p.m., and gave her medication to help her function.

Now, more than five years after the shooting, Lawson no longer has daily panic attacks, and said she's in a much better place. She said that eye movement desensitization and reprocessing therapy helped her manage her triggers. She has continued to go to various forms of therapy since the shooting.

"I don't want people to think that it's just kind of this bleak outcome that you're always you know going to be severely traumatized," she said. "You do get better."

Still, it is hard for her to hear about new shootings.

"They bring back the pain that you feel right after the experience that you've had and they can be also very triggering," she said. "When I do hear about recent shootings and tragedies a lot of times I will begin to have nightmares again. My anxiety ramps up."

When she hears about the latest tragedies, Lawson makes sure to reach out for support. Often, she'll ask someone to go with her if she needs to go to the grocery store, or if she thinks she'll encounter any other triggers. She, however, said that after tragedies she tends to stay home a little more.

One thing that helps Lawson, in addition to her therapy, is working with The Rebels Project, a volunteer community outreach non-profit founded by Columbine survivors that provides support to people after trauma.

"Just hearing Columbine survivors talk about some things that they continue to struggle with in life was very validating for me and it helped me to feel less almost abnormal or like there was something just damaged or wrong with me because I was still struggling too," she said.

It's important to seek help after a traumatic event, Lawson said. But she said that sometimes needing help is stigmatized. She said that some of her own friends and people in her support system didn't understand why she was still struggling several months after the Washington Navy Yard shooting.

"A couple of them, you know, questioned it. I was told by one friend that I was choosing to dwell on what happened and be depressed. ... Statements like that weren't very beneficial and I really began to isolate and just stay to myself," she said.

An important step for many survivors is to break through the stigma around mental health and around seeking therapy, Lawson said. She also said it's important not to invalidate survivors' experiences."""

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = np.array(Image.open('boy.jpg'))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="black", mask=alice_mask,
               stopwords=stopwords, contour_width=10, contour_color='steelblue')

# generate word cloud
wc.generate(text)

# store to file
wc.to_file('parth_cloud.jpg')

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()