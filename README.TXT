This experiment uses enhanced suffix arrays to compute all the repeated
phrases a speech. The 2011 State of the Union Address was used as the text.

Here are the longest 
phrases that are repeated. Length is measured in terms
of the number of words:

repeats length          phrase
--------------------------------------------------------------------
3       4       '. that dream is why '
2       5       ' a government that's more '
2       5       ' of a small business owner '
2       5       ' over the last two years '
2       5       ' over the next ten years, '
2       5       ' that says this is a '
2       5       ' us apart as a nation. '
2       5       '. because you deserve to know '
2       5       '. what comes of this moment '
3       5       ' i'm not willing to '
3       6       ' step in winning the future is '
2       11      ' if you want to make a difference in the life of '

' if you want to make a difference in the life of ' is used in an interesting
analogy between a child and a nation:
"If you want to make a difference in the life of our nation; 
if you want to make a difference in the life of a child – become a teacher. Your country needs you.""

"step in winning the future is" was repeated three times.
The listing of the steps was not very clear in the speech.

1. The first step in winning the future is encouraging American innovation.
2. The third step in winning the future is rebuilding America. 
3. Now, the final step – a critical step – in winning the future is to make sure we aren't buried under a mountain of debt.

This looks kind of bungled. There is no second step in the transcript as far as I can tell.
I hope the transcripts are off and that the speech was better.

It is very interesting that the phrase "I'm not willing to" is repeated three times.
Sometimes the most important thing someone is about is what they are not about.
This speech is trying to give the impression that the president is holding up his
will against an unnamed force. That force is obviously the Republican party. But I don't
think that the resistance is that strong. Had he named names, it would have been more believable.


sorted-by-frequency.txt has the phrases sorted by frequency.

The bottom of the file is loaded with stop words and common punctuation
214     1       ' to '
214     1       ' to '
235     1       ' and '
336     0       ', '
344     0       ','
352     1       ' the '
403     0       '.'


If we look further up the list of words in decreasing frequency, the
first word that we see that is not very common word is "people".
I don't have a handy measure of a words frequency relative to the
whole of everyday speech. Still this is a strong intuition that
"people" jumps out as the odd word. 

22      1       ' make '
22      1       ' people '
22      1       '. but '
23      1       ' you '
23      1       ', but '
23      1       ', but '
24      1       ' all '

Over all it is probably good that a president is using the word "people"
22 times during a speech. If he said "congress" 22 times, I would be more
worried.

List of files & directories

README.TXT  - this file
attic - a place to store old files
interesting-repeats.txt - a list of long repeating phrases
output.txt - the output of repeating-phrases.py
repeating-phrases.py - a Python program that computes all the repeating phrases
sorted-by-frequency.txt - the output sorted by frequency
sorted-by-words-length.txt - the ouput sorted by the length of the repeated phrase
state of the union 2011 lowercased ascii.txt - a transcript of the 2011 state of union speech
temp.txt - output.txt with the top few header lines removed, makes for easier command-line sorting


List of things to TO DO:
1. add a command-line interface to repeating-phrases
2. document each function
3. find a simple linear suffix array construction
4. plot the run time as the input text increases in length
5. put together a collection of sample text of writters known for interesting and
   unusual phrases that are repeatedly used in their writing
