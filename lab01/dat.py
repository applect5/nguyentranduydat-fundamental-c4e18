from gmail import *
from random import choice
gmail=GMail('nguyenduydat1027@gmail.com','dat12345678')
html_content="""
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Cộng ho&agrave; x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc Lập - Tự Do -Hạnh Ph&uacute;c</p>
<p style="text-align: center;"><strong> Đơn xin nghỉ học </strong></p>
<p>Em ch&agrave;o anh</p>
<p>T&ecirc;n em l&agrave; Nguyễn Trần Duy Đạt</p>
<p>H&ocirc;m nay em viết đơn n&agrave;y để xin nghỉ học buổi học sắp tới. L&iacute; do h&ocirc;m nay bị ng&atilde; {{abc}}. Em xin hứa sẽ học b&agrave;i v&agrave; l&agrave;m b&agrave;i đầy đủ.Em xin cảm ơn anh.</p>
<p>&nbsp;</p>
<p>Duy Đạt handsome.</p>
"""
#placeholder 
mylist = ['Gãy tay','Gãy cổ','Gãy lưng','Gãy mũi','Gãy móng tay']
reason = choice(mylist)
html_content_to_sent = html_content.replace("{{abc}}", reason)

msg=Message('Hello mother fucker',to='duydat75@gmail.com',
                html=html_content_to_sent)

gmail.send(msg)