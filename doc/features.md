#### الوظائف- الدوال

##### أهم الوظائف

وصف الدالة  |الدالة
------|------------
حذف الحركات كلها بما فيها الشدة|strip_tashkeel(text)
حذف الحركات كلها ماعدا الشدة|strip_harakat(text)
حذف الحركة الأخيرة|strip_lastharaka(text)
حذف التطويل| strip_tatweel(text)
تنميط أشكال الهمزة المختلفة | normalize_hamza(text)
تفريق كلمات النص |tokenize(text)

* حذف الحركات

 * حذف كل الحركات عدا الشدة

Strip Harakat from arabic word except Shadda. The striped marks are :
Example:

```python
>>> text = u"الْعَرَبِيّةُ"
>>> strip_harakat(text)
>>> العربيّة
```
 * حذف الحركات بما فيها الشدة

Strip vowels from a text, include Shadda. The striped marks are :

```python
>>> text = u"الْعَرَبِيّةُ"
>>> strip_tashkeel(text)
العربية
```

 * حذف الحركة الأخيرة فقط:
 قد تكون هي الحركة الإعرابية، لكن ليس في كل الحالات، مثلا يضربه، حركة الإعراب على الباء وليس على الهاء

Strip the last Haraka from arabic word except Shadda. The striped marks are :
```python
>>> text = u"الْعَرَبِيّةُ"
>>> strip_lastharaka(text)
الْعَرَبِيّة
```

 * اختزال التشكيل 
Reduce the Tashkeel, by deleting evident cases.

```python
>>> word = u"يُتَسََلَّمْنَ"
>>> reduced = araby.reduce_tashkeel(word)
>>> print reduced.encode('utf8')
يُتسلّمن
```

*  حذف التطويل أو الشدة

Strip tatweel or Shadda from a text.

```python
>>> text = u"العـــــربية"
>>> strip_tatweel(text)
العربية
>>> text = u"الشّمسيّة"
>>> strip_shadda(text)
 الشمسية
```
 
* تنميط الحروف المركبة والهمزة

بعض البرامج تعطي حروف متراكبة، توحيدها يرجعها إلى حروف بسيطة

Normalize Lam Alef ligatures into two letters (LAM and ALEF)
    LAM_ALEF, LAM_ALEF_HAMZA_ABOVE, LAM_ALEF_HAMZA_BELOW, LAM_ALEF_MADDA_ABOVE
```python
>>> text = u"لانها لالء الاسلام"
>>> normalize_ligature(text)
لانها لالئ الاسلام
```

 * توحيد الهمزة

Standardize the Hamzat into one form of hamza, replace Madda by hamza and alef. Replace the LamAlefs by simplified letters.

```python
>>> text = u"سئل أحد الأئمة"
>>> normalize_hamza(text)
 سءل ءحد الءءمة
```

* فصل الحركات والحروف

يمكن استخلاص الحروف والحركات في سلسلتين متوازيتين، بحيث يقابل كل حرف حركة محددة، إذا غابت الحركة رمزنا لها بتطويل

separate the letters from the vowels, in arabic word, if a letter hasn't a haraka, the not definited haraka is attributed. return ( letters, vowels)

```python
>>> araby.separate(text)
(u'\u0627\u0644\u0639\u0631\u0628\u064a\u0629', u'\u064e\u0652\u064e\u064e\u064e\u064e\u064f')
>>> letters, marks =araby.separate(text)
>>> print letters.encode('utf8')
العربية
>>> print marks.encode('utf8')
>>> for m in marks:
...     print araby.name(m)
فتحة
سكون
فتحة
فتحة
فتحة
فتحة
ضمة
```
يمكن دمج الحركات والحروف في كلمة واحدة، شرط أن يكون طول السلسلتين متساويا.
ينوب عن غياب الحركة حرف التطويل

joint the letters with the marks the length ot letters and marks must be equal return word

```python
>>> letters = u"العربية"
>>> marks   = u'\u064e\u0652\u064e\u064e\u064e\u064e\u064f'
>>> word = araby.joint(letters, marks)
>>> print word.encode('utf8')
اَلْعَرَبَيَةُ
```

* حساب التماثل

التماثل في الحركات بين كلمتين يون صحيحا 
إذا كان للكلمتين نفس الحروف، ونفس الحركات، ولو كانت الحركات ناقصة 

if the two words has the same letters and the same harakats, this fuction return True. The two words can be full vocalized, or partial vocalized

```python
>>> word1 = u"ضَربٌ"
>>> word2 = u"ضَرْبٌ"
>>> araby.vocalizedlike(word1, word2)
True
```

 * تماثل الوزن
تتماثل كلمة مع وزن إذا كانت الحروف تتطابق مع الوزن  والحركات مع الحركات، يمكن أن يكون التشكيل غير كامل

If the word1 is like a wazn (pattern), the letters must be equal, the wazn has FEH, AIN, LAM letters. this are as generic letters. The two words can be full vocalized, or partial vocalized

```python
>>> word1 = u"ضارب"
>>> wazn =  u"فَاعِل"
>>> araby.waznlike(word1, wazn)
True
```

 * تتماثل كلمتان في الشدة إذ كانت لهما نفس المكان، والحركات أيضا
وقد يكون التشكيل غير كامل

If the two words has the same letters and the same harakats, this fuction return True. The first word is partially vocalized, the second is fully if the partially contians a shadda, it must be at the same place in the fully

```python
>>> word1 = u"ردّ"
>>> word2=u"ردَّ"
>>> araby.shaddalike(word1, word2)
True
```

 * حساب التماثل في الحركات

نقيس التماثل في الحركات ، بحيث كل اختلاف ننقص 1
فنحصل على عدد سالب حسب عدد مرات الاختلاف

if the two words has the same letters and the same harakats, this function return True. The two words can be full vocalized, or partial vocalized

```python
>>> word1 = u"ضَربٌ"
>>> word2 = u"ضَرْبٌ"
>>> araby.vocalizedlike(word1, word2)
True
>>> word1 = u"ضَربٌ"
>>> word2 = u"ضَرْبٍ"
>>> araby.vocalized_similarity(word1, word2)
-1
```

*  تفريق النص

يمكن استعمال الدالة tokenize لتفريق النص إلى كلمات

Tokenize text into words.

```python 
>>> text = u"العربية لغة جميلة."
>>> tokens = araby.tokenize(text)
>>> print u"\n".join(tokens)
‎العربية
‎لغة
‎جميلة
.

```
You can use it with conditions (restrict Arabic, keep or remove numbers, exclude stop words ...etc).

To remove tashkeel and filter out non-Arabic words:
```python
>>> text = u"ِاسمٌ الكلبِ في اللغةِ الإنجليزية Dog واسمُ الحمارِ Donky"
>>> tokenize(text, conditions=is_arabicrange, morphs=strip_tashkeel)
        ['اسم', 'الكلب', 'في', 'اللغة', 'الإنجليزية', 'واسم', 'الحمار']
```
This structure will enable us to create functions on the fly and pass them:       
```python
>>> text = u"طلع البدر علينا من ثنيات الوداع"
>>>tokenize(text, conditions=lambda x: x.startswith(u'ال'))
        ['البدر', 'الوداع']
```    




#### وظائف الحروف
دوال الحروف وهي تعيد صواب إذا انتمى الحرف إلى المجموعة المطلوبة

وصف الدالة  |الدالة
------|------------
إذا كان الحرف المعطى سكونا يرجع صحيح | is_sukun(archar)
إذا كان الحرف المعطى شدة يرجع صحيح | is_shadda(archar)
إذا كان الحرف المعطى تطويلا يرجع صحيح | is_tatweel(archar)
إذا كان الحرف المعطى تنوينا يرجع صحيح | is_tanwin(archar)
إذا كان الحرف المعطى تشكيلا (حركة أو شدة) يرجع صحيح | is_tashkeel(archar)
إذا كان الحرف المعطى حركة يرجع صحيح | is_haraka(archar)
إذا كان الحرف المعطى حركة قصيرة يرجع صحيح | is_shortharaka(archar)
إذا كان الحرف المعطى لام ألف يرجع صحيح | is_ligature(archar)
إذا كان الحرف المعطى همزة يرجع صحيح | is_hamza(archar)
إذا كان الحرف المعطى ألفا يرجع صحيح | is_alef(archar)
إذا كان الحرف المعطى يماثل الياء في رسمه يرجع صحيح | is_yehlike(archar)
إذا كان الحرف المعطى يماثل الواو في رسمه يرجع صحيح | is_wawlike(archar)
إذا كان الحرف المعطى تاء مفتوحة أو مربوطة يرجع صحيح | is_teh(archar)
إذا كان الحرف المعطى حرفا صغيرا يرجع صحيح | is_small(archar)
إذا كان الحرف المعطى حرف علة يرجع صحيح | is_weak(archar)
إذا كان الحرف المعطى حرفا قمريا يرجع صحيح | is_moon(archar)
إذا كان الحرف المعطى حرفا شمسيا يرجع صحيح | is_sun(archar)

### مثال

في نطق الأسماء يتحوّل الحرف الشمسي بعد ال التعريف إلى حرف مشدد أي أنّ "الشمس" تنطق "أششمس"، 
```python
#!/usr/bin/python
# -*- coding=utf-8 -*-
import pyarabic.araby as araby
words=[u'الشمس', u'القمر', u'الرجل', u'بصل', u'البصل']
for word in words:
    if word.startswith(araby.ALEF+araby.LAM) and araby.isSun(word[2]):
        word=u''.join([araby.ALEF+word[2],word[2:]]);
    print word.encode('utf8');
```
في المثال، نعطي عددا من الكلمات لكتابة نطقها، بتحويل الحرف الشمسي بعد ال التعريف إلى حرف مكرر والنتيجة تكون 
```
اششمس
القمر
اررجل
بصل
البصل
```

# وظائف الأعداد والأرقام
number.py
توفر هذه المكتبة وظائف مثل : 
 * تحويل عدد إلى كلمات
 * البحث عن مواضع العبارات العددية
 * تحويل الكلمات إلى أعداد، 
 * استخلاص العبارات العددية
 * تشكيلها
 
* تحويل عدد إلى كلمات
Convert number to words
```python
>>>import pyarabic.number
>>>an = pyarabic.number.ArNumbers()
>>>an.int2str('125')
مئة و خمسة وعشرون

```
* تحويل الكلمات إلى أعداد
Convert arabic text into number, for example convert تسعة وعشرون = >29.

```python
>>> text2number(u"خمسمئة وثلاث وعشرون")
523
```

* تشكيل جملة كلمات عددية
Vocalize a number words clause

```python
>>> txt = u"خمسمئة وثلاثة وعشرين"
>>> wordlist = araby.tokenize(txt)
>>> vocalized =  vocalize_number(wordlist)
>>> print u" ".join(vocalized)
خَمْسمِئَة وَثَلاثَة وَعِشْرِينَ
>>>
```

* استخلاص العبارات العددية من جملة

Extract number words in a text.

```python
>>> extract_number_phrases(u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا")
خمسمئة وثلاثة وعشرين
ثلاثة عشر
```

* استخلاص العبارات العددية مع سياقها

Extract number words in a text with context.

```python
>>> extract_number_context(u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا")
‎وجدت، خمسمئة وثلاثة وعشرين، دينارا
‎فاشتريت، ثلاثة عشر ، دفتر
```

* استخلاص مواضع العبارات العددية

Detect number words in a text and return positions of each phrase.

```python
>>> txt = u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا"
>>> wordlist = araby.tokenize(txt)
>>> positions_phrases =  detect_number_phrases_position(wordlist)
>>> print positions_phrase
>>> print positions_phrases
[(1, 3), (6, 7)]
```

* استخلاص مواضع العبارات العددية باستعمال الوسوم 

 * DO: لاشيء
 * DB: بداية العبارة العددية
 * BI: داخل العبارة العددية

Detect number words in a text and return a taglist as BIO.

```python
>>> wordlist = araby.tokenize(u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا")
>>> detect_numbers(wordlist)
['DO', 'DB', 'DI', 'DI', 'DO', 'DO', 'DB', 'DI', 'DO']
```

* استخلاص العبارات العددية وإرجاع الجمل

Detect number words in a text, return strings.

```python
>>> detect_number_words(u"وجدت خمسمئة وثلاثة وعشرين دينارا")
خمسمئة وثلاثة وعشرين
```
* تشكيل أولي للعبارات العددية

Vocalized a number clauses in a text.

```python
>>> txt = u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا"
>>> wordlist = araby.tokenize(txt)
>>> vocalized =  pre_tashkeel_number(wordlist)
>>> print u" ".join(vocalized)
وجدت خَمْسمِئَة وَثَلاثَة وَعِشْرِينَ دينارا فاشتريت ثَلاثَةَ عَشَرَ دفترا
```


#### وظائف قلب النصوص
تستعمل لقلب الحروف، بسبب عدم دعم بعض البرامج للغة العربية، مما يدعونا إلى قلب الحروف.

* قلب النص 

Unshape a text

```python 
>>> TEXTS = u'لو والحيـاة مريرة   وليتك ترضى والانـــام غضاب '
>>> print unshaping_text(TEXTS).encode('utf8')
باضغ ماـــنالاو ىضرت كتيلو   ةريرم ةاـيحلاو ولحت كتيلف

```
* قلب سطر

Unshape a line

```python
>>> line = u'فليتك تحلو والحيـاة مريرة   وليتك ترضى والانـــام غضاب '
>>> print unshaping_line(line).encode('utf8')
باضغ ماـــنالاو ىضرت كتيلو   ةريرم ةاـيحلاو ولحت كتيلف

```
* قلب كلمة

Unshape a word
```python
>>> word = u'العربية'
>>> print unshaping_word(word).encode('utf8')
ةيبرعلا
```


