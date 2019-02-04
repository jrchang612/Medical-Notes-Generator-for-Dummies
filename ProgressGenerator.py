#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 11:16:34 2019

@author: jrchang612
"""
Stop = False
Paragraph = []
MaleFemale = {'M': 'male', 'F':'female'}
menWoman = {'M': 'man', 'F': 'woman'}
heShe = {'M':'he', 'F':'she'}
hisHer = {'M': 'his', 'F':'her'}
himHer = {'M': 'him', 'F':'her'}
HeShe = {'M':'He', 'F':'She'}
HisHer = {'M': 'His', 'F':'Her'}
HimHer = {'M': 'Him', 'F':'Her'}
wasWere ={1: 'was', 2: 'were'}
MethodList = {'G':'reset gender', 'Age': 'reset age', 'T':'This is a ...', 'TT': 'This time...', \
              'ER':'Therefore, he/she was sent to our ER ...', 'Img':'Image showed ...',\
              'Imp':'Under the impression of ..., he/she was admitted to ...',\
              'A': 'after admission/transferral...', 'D': '...was done', 'Anti': 'add or DC antibiotics',\
              'Cond': 'His/Her condition was...', 'H':'However, ...', 'TR': 'transfer',\
              'RM': '... was removed on ...', 'DC': 'discharge', \
              'FS':'freestyle', 'SP': 'separate paragraph','S': 'show paragraph', \
              'AntiList': 'generate antibiotics list','stop': 'end program',\
              'DEMO':'Print demo medical note.'}
class Switcher(object):
    def ChooseMethods(self, argument):
        method_name = str(argument)
        method = getattr(self, method_name, lambda: "Invalid Input")
        return method()
    def G(self, argument):
        TF = True
        self.anti = {'Antibiotics':['Start Date', 'End Date']}
        while(TF):
            self.gender = argument
            if argument in MaleFemale.keys():
                print('This is a %s patient.' %(MaleFemale[self.gender]))
                TF = False
            else:
                print('Incorrect gender code. Enter M or F.')
                argument = input('Enter the gender of the patient(M/F): ')
    def Age(self):
        argument = input('Enter the age of the patient(e.g. 53y/o): ')
        self.age = argument
    def A(self):
        Sent = 'After '
        d0 = {'1':'admission, ', '2': 'transferral, '}
        print(Sent)
        Paragraph.append(Sent)
        print(d0)
        SELECT0 = input('Enter choice: ')
        Paragraph.append(d0[SELECT0])
        d1 = {'1':'we monitored %s vital signs and clinical conditions closely. ' %(hisHer[self.gender]), \
              '2':'there were no contraindications to '}
        print(d1)
        SELECT1 = input('Enter choice: ')
        if SELECT1 == '1':
            Paragraph.append(d1[SELECT1])
        else:
            d2 = {'1': 'surgery. ', '2': 'chemotherapy. ', '3':'target therapy. ', '4':'Rituximab. '} 
            print(d2)
            SELECT2 = input('Enter choice: ')
            Paragraph.append(d1[SELECT1])
            Paragraph.append(d2[SELECT2])
        return 
    def DC(self):
        DATE = input('Enter discharge date: ')
        OPD = input('Enter OPD: ')
        if OPD.find(',') != -1:
            key_wasWere = 2
        else: key_wasWere = 1
        Sent = 'Under stable conditions, %s was discharged on %s, and %s OPD follow up %s arranged. ' \
        %(heShe[self.gender], DATE, OPD, wasWere[key_wasWere])
        Paragraph.append(Sent)
        return 
    def TR(self):
        DATE = input('Enter transferral date: ')
        WHERE = input('Transfer to where? ')
        d = {'1': 'stable', '2': 'unstable', '3':'critical'}
        print(d)
        SELECT = input('Enter the condition of the patient: ')
        Sent = 'Under %s condition, %s was transferred to %s on %s for further management. '\
        %(d[SELECT], heShe[self.gender], WHERE, DATE)
        Paragraph.append(Sent)
        return
    def S(self):
        s = ''.join(Paragraph)
        print(s)
        return
    def D(self):
        DATE = input('Enter date: ')
        WWD = input('What was done: ')
        if WWD.find(',') != -1:
            key_wasWere = 2
        else: key_wasWere = 1
        Sent = '%s %s done on %s' %(WWD, wasWere[key_wasWere], DATE)
        print(Sent)
        d_NEXT = {'1':', and %s tolerated the procedure well. ' %(heShe[self.gender]), '2':'. '}
        print(d_NEXT)
        NEXT = input('Enter choice: ')
        Paragraph.append(Sent)
        Paragraph.append(d_NEXT[NEXT])
    def FS(self):
        Sent = input('Enter sentence: ')
        Paragraph.append(Sent)
    def RM(self):
        THING = input('What was removed? ')
        DATE = input('Enter date: ')
        YN = input('follow up CXR?(Y/N)')
        if YN == 'Y':
            Sent2 = ', and follow up CXR showed no evidence of pneumothorax. '
        else: Sent2 = '.'
        if THING.find(',') != -1:
            key_wasWere = 2
        else: key_wasWere = 1
        Sent1 = '%s %s removed on %s' %(THING, wasWere[key_wasWere], DATE)
        Paragraph.append(Sent1)
        Paragraph.append(Sent2)
    def SP(self):
        sent = '\n\n'
        Paragraph.append(sent)
    def T(self):
        Sent1 = 'This is a %s %s with ' %(self.age, menWoman[self.gender])
        d = {'1': 'no known underlying diseases. ', '2': 'history of:'}
        print(Sent1)
        print(d)
        Choice = input('Enter choice: ')
        if Choice == '1':
            Paragraph.append(Sent1)
            Paragraph.append(d[Choice])
        else:
            i = 1
            Sent2 = []
            keep = True
            while(keep):
                a = input('Enter underlying disease (press Enter to skip):')
                if a != '':
                    Sent2.append('\n%d. %s' %(i, a))
                    i+=1
                else: 
                    s = ''.join(Sent2)
                    keep = False
            Paragraph.append(Sent1)
            Paragraph.append(s)
            Paragraph.append('\n')
    def TT(self):
        print('This time, ... was noted since ....')
        WHAT = input('What was noted? ')
        TIME = input('Since when/for how long?(e.g. since 2018/10, for 30 minutes, ...) ')
        Sent1 = 'This time, %s was noted %s. ' %(WHAT, TIME)
        Paragraph.append(Sent1)
    def Cond(self):
        Choice = input('His/Her condition was (1)stationary (2)stable (3)improving (4)deteriorating since then. ')
        d = {'1': 'stationary', '2': 'stable', '3':'improving', '4':'deteriorating'}
        Sent = '%s condition was %s since then. ' %(HisHer[self.gender], d[Choice])
        Paragraph.append(Sent)
    def H(self):
        print('However, ... was noted on ...')
        DATE = input('When did it happen? ')
        d0 = {'1': 'fever up to *** was noted ', '2':'%s turned delirious' %(heShe[self.gender]),\
             '3':'%s GCS was down to ***' %(hisHer[self.gender]), '4':'freestyle'}
        print(d0)
        Choice0 = input('Enter choice: ')
        if Choice0 == '1':
            DEG = input('fever up to ??? was noted: ')
            d1 = {'1':'Septic workup was done. ',\
                  '2':'Septic workup was done, and *** was added. ',\
                  '3':'Septic workup was done, and antibiotics was shifted from *** to ***.'}
            print(d1)
            Choice1 = input('Enter choice: ')
            d2 = {'1':'for better GPC coverage. ', '2':'for better GNB coverage. ', '3':'for better anaerobic coverage. ',\
              '4':'for better fungus coverage. ', '5':'for better coverage on atypical pathogens. ',\
              '6':'according to the culture result and sensitivity testing. ', '7':'empirically. ',\
              '8':'freestyle', '9':'. '} 
            if Choice1 == '1':
                Sent = 'However, fever up to %s was noted on %s; septic workup was done.'%(DEG, DATE)
                Paragraph.append(Sent)
            elif Choice1 == '2':
                ANTI = input('What antibiotic was added? ')
                self.anti[ANTI] = ['','']
                self.anti[ANTI][0] = DATE
                print(d2)
                Choice2 = input('Enter choice:')
                if Choice2 == '8':
                    Sent2 = input('add a reason: ')
                    Sent1 = 'However, fever up to %s was noted on %s; septic workup was done, and %s was added '%(DEG, DATE, ANTI,)
                    Paragraph.append(Sent1)
                    Paragraph.append(Sent2)
                else:
                    Sent1 = 'However, fever up to %s was noted on %s; septic workup was done, and %s was added '%(DEG, DATE, ANTI)
                    Paragraph.append(Sent1)
                    Paragraph.append(d2[Choice2])
            elif Choice1 =='3':
                ANTI1 = input('Which antibiotic was used before? ')
                ANTI2 = input('Which antibiotic was used after? ')
                self.anti[ANTI1][1] = DATE
                self.anti[ANTI2] = ['','']
                self.anti[ANTI2][0] = DATE
                print(d2)
                Choice2 = input('Enter choice: ')
                if Choice2 == '8':
                    Sent2 = input('add a reason: ')
                    Sent1 = 'However, fever up to %s was noted on %s; septic workup was done, and antibiotics was shifted from %s to %s '%(DEG, DATE, ANTI1, ANTI2,)
                    Paragraph.append(Sent1)
                    Paragraph.append(Sent2)
                else:
                    Sent1 = 'However, fever up to %s was noted on %s; septic workup was done, and antibiotics was shifted from %s to %s '%(DEG, DATE, ANTI1, ANTI2)
                    Paragraph.append(Sent1)
                    Paragraph.append(d2[Choice2])  
        elif Choice0 == '4' :
            WHAT = input('What was noted? ')
            DOES = input('What did you do? ')
            Sent1 = 'However, %s was noted on %s. ' %(WHAT, DATE)
            Paragraph.append(Sent1)
            Paragraph.append(DOES)
        elif Choice0 == '2':
            DOES = input('What did you do? ')
            Sent1 = 'However, %s turned delirious on %s. ' %(heShe[self.gender], DATE)
            Paragraph.append(Sent1)
            Paragraph.append(DOES)
        elif Choice0 == '3':
            GCS = input('What was his/her new conscious level? ')
            Sent1 = 'However, %s GCS was down to %s on %s. '%(hisHer[self.gender], GCS, DATE)
            Choice1 = input('(1)nothing (2)mannitol (3)hypertonic salie (4)both was given.')
            d3 = {'1': ' ', '2':'Mannitol was given. ', '3':'Hypertonic saline was given. ', '4':'Mannito and hypertonic saline were given. '}
            Sent2 = d3[Choice1]
            Paragraph.append(Sent1)
            Paragraph.append(Sent2)
            Choice2 = input('Emergent CT was done? (1)Yes (2)No. ')
            if Choice2 == '1':
                Finding = input('What did the CT show?(e.g. a new hematoma over left parietal lobe, progressed hydrocephalus,...)')
                Sent3 = 'Emergent CT was done, which showed %s' %(Finding)
                Paragraph.append(Sent3)
    def Anti(self):
        Choice0 = input('Any new culture/lab results? (1)Yes (2)No. ')
        d1 = {'1':'after completing a 5-day course. ', '2':'after completing a 7-day course. ',\
              '3':'after completing a 10-day course. ', '4':'after completing a 14-day course. ',\
              '5':'due to lack of culture evidence. ', '6':'freestyle', '7':'. '}
        d2 = {'1':'for better GPC coverage. ', '2':'for better GNB coverage. ', '3':'for better anaerobic coverage. ',\
              '4':'for better fungus coverage. ', '5':'for better coverage on atypical pathogens. ',\
              '6':'according to the culture result and sensitivity testing. ', '7':'empirically. ',\
              '8':'freestyle', '9':'post-operatively. ', '10':'. '}        
        if Choice0 == '1':
            EVID = input('Which evidence?(e.g. Sputum culture, Aspergillus antigen,... )')
            DATE0 = input('Date of the culture/lab: ')
            WHAT = input('What happened?(e.g. grew WT-PsA, was positive,... )')
            Paragraph.append('%s on %s %s. ' %(EVID, DATE0, WHAT))
        Choice1 = input('ANTI was (1)given (2)discontinued (3)changed from A to B on ... for ...')
        if Choice1 == '1':
            ANTI = input('What antibiotic was given? ')
            DATE = input('When was it given? ')
            self.anti[ANTI] = ['','']
            self.anti[ANTI][0] = DATE
            print(d2)
            Choice2 = input('Enter choice:')
            if Choice2 == '8':
                Sent2 = input('add a reason: ')
                Sent1 = '%s was given on %s '%(ANTI, DATE)
                Paragraph.append(Sent1)
                Paragraph.append(Sent2)
            else:
                Sent1 = '%s was given on %s '%(ANTI, DATE)
                Paragraph.append(Sent1)
                Paragraph.append(d2[Choice2])
        elif Choice1 == '2':
            ANTI = input('What antibiotic was discontinued? ')
            DATE = input('When was it discontinued? ')
            self.anti[ANTI][1] = DATE
            print(d1)
            Choice2 = input('Enter choice: ')
            if Choice2 == '6':
                Sent2 = input('add a reason: ')
                Sent1 = '%s was discontinued on %s '%(ANTI, DATE)
                Paragraph.append(Sent1)
                Paragraph.append(Sent2)
            else:
                Sent1 = '%s was discontinued on %s '%(ANTI, DATE)
                Paragraph.append(Sent1)
                Paragraph.append(d1[Choice2])
        elif Choice1 =='3':
            ANTI1 = input('Which antibiotic was used before? ')
            ANTI2 = input('Which antibiotic was used after? ')
            DATE = input('When was it changed? ')
            self.anti[ANTI1][1] = DATE
            self.anti[ANTI2] = ['','']
            self.anti[ANTI2][0] = DATE
            print(d2)
            Choice2 = input('Enter choice: ')
            if Choice2 == '8':
                Sent2 = input('add a reason: ')
                Sent1 = '%s was shifted to %s on %s '%(ANTI1, ANTI2, DATE)
                Paragraph.append(Sent1)
                Paragraph.append(Sent2)
            else:
                Sent1 = '%s was shifted to %s on %s '%(ANTI1, ANTI2, DATE)
                Paragraph.append(Sent1)
                Paragraph.append(d2[Choice2])               
    def AntiList(self):
        Paragraph.append('\n\n')
        for keys in self.anti:
            a = '%s: %s ~ %s\n'%(keys, self.anti[keys][0], self.anti[keys][1])
            Paragraph.append(a)
    def Imp(self):
        Impression = input('What was your impression? ')
        DATE = input('Admission date? ')
        WHERE = input('Where was he/she admitted?(e.g. nephrology ward, SICU, ...)')
        Sent='Under the impression of %s, %s was admitted to %s on %s for further management.'\
        %(Impression, heShe[self.gender], WHERE, DATE)
        Paragraph.append(Sent)
    def ER(self):
        DATE = input('When did he/she visit our ER?(e.g. 2019/01/02 13:30)')
        T = input('His/her temperature upon arrival? ')
        P = input('His/her heart rate upon arrival? ')
        R = input('His/her respiratory rate upon arrival? ')
        BP = input('His/her blood pressure upon arrival? ')
        Sat = input('His/her saturation upon arrival?(e.g. 98%(RA)) ')
        IntVS = input('Interpretation of vitals?(e.g. marked tachycardia with hypotension, ...) ')
        PE = input('What did physcial exam show?(e.g. marked intercostal retraction, orthopnea, ...) ')
        Sent1 = 'Therefore, %s was sent to our ER on %s. Upon arrival, %s vital signs showed %s(T:%s, P:%s, R:%s, BP:%s, Sat:%s). Physical examinations revealed %s. '\
        %(heShe[self.gender], DATE, hisHer[self.gender], IntVS, T, P, R, BP, Sat, PE)
        Lab = input('Any lab data?(e.g. ABG showed profound metabolic acidosis without proper compensation; his/her lab data showed AKI and hyperkalemia up to 6.3.) ')
        Paragraph.append(Sent1)
        Paragraph.append(Lab)
    def Img(self):
        dImg = {'1':'CXR ', '2':'KUB ','3':'Noncontrast CT ','4':'Contrast CT ','5':'Angiography ','6':'FAST scan ','7':'MRI ','8':'Other modalities'}
        print(dImg)
        Choice0 = input('Choose modality: ')
        if Choice0 =='8':
            Mod = input('What was the image modality? ')
        else: Mod = dImg[Choice0]
        Finding = input('What did the image show?(e.g. an ICH upto 60cc in her left occipital lobe, bilateral increased infiltration and cardiomegaly,...) ')
        DATE = input('When was it done? ')
        Sent = '%s was done on %s, which revealed %s. '%(Mod, DATE, Finding)
        Paragraph.append(Sent)
    def DEMO(self):
        print('Type the following command sequentially to generate the demo medical note.')
        print('M')
        print('73y/o')
        print('T')
        print('2')
        print('Lung cancer, ADCA, LUL, s/p VATS LUL lobectomy on 2018/10')
        print('DM')
        print('HTN')
        print('dyslipidemia')
        print('gout')
        print('\n')
        print('TT')
        print('severe abdominal pain over LLQ')
        print('for 3 days')
        print('FS')
        print('The pain was dull, with a pain score of 6 on a pain scale ranging from 0 to 10, and was accompanied by severe nausea and vomiting. The pain was slightly improved by lying flat. ')
        print('ER')
        print('2019/02/02 15:47')
        print('38.1')
        print('122')
        print('21')
        print('131/70')
        print('97%(RA)')
        print('fever and marked tachycardia')
        print('marked RLQ tenderness and positive McBurney sign')
        print('Lab data showed marked leukocytosis and elevated CRP up to 8.3. ')
        print('Img')
        print('4')
        print('A-colon diverticulitis without rupture or abscess formation')
        print('the same day')
        print('Imp')
        print('A-colon diverticulitis')
        print('2019/02/03')
        print('GS general ward')
        print('SP')
        print('A')
        print('1')
        print('1')
        print('FS')
        print('Medical Treatment was suggested first.')
        print('Anti')
        print('2')
        print('1')
        print('Flumarin')
        print('2019/02/02')
        print('7')
        print('Cond')
        print('3')
        print('H')
        print('2019/02/10')
        print('1')
        print('39.1')
        print('3')
        print('Flumarin')
        print('Mepem')
        print('7')
        print('FS')
        print('Physical examination showed coarse crackles over RLL lung field, and CXR showed a new pneumonia patch over RLL. Desaturation, marked tachycardia and mild hypotension was noted later. We gave fluid challenge and O2 mask support, and his blood pressure and saturation improved. ') 
        print('TR')
        print('2019/02/10')
        print('SICU')
        print('2')
        print('SP')
        print('A')
        print('2')
        print('1')
        print('D')
        print('2019/02/10')
        print('CVC placement')
        print('1')
        print('FS')
        print('Levophed was given, and we soon tapered it off.')
        print('Anti')
        print('1')
        print('Sputum culture and blood culture')
        print('2019/02/10')
        print('both grew wild-type Pseudomonas aeruginosa')
        print('3')
        print('Mepem')
        print('Fortum')
        print('2019/02/13')
        print('6')
        print('Cond')
        print('3')
        print('TR')
        print('2019/02/15')
        print('general ward')
        print('1')
        print('SP')
        print('A')
        print('2')
        print('1')
        print('Anti')
        print('2')
        print('2')
        print('Fortum')
        print('2019/02/24')
        print('4')
        print('RM')
        print('CVC')
        print('the same day')
        print('N')
        print('Cond')
        print('2')
        print('DC')
        print('2019/02/25')
        print('GS, CS')
        print('AntiList')
        print('S')
        return
        
#    def save(self):
#        text_file = open("Note.txt", "w")
#        s = ''.join(Paragraph)
#        text_file.write(s)
#        text_file.close()

Main=Switcher()
print('\nThis program was made by jrchang612 in 2019/02, ver.1.\n')
print(MethodList)
Main.G(input('Enter the gender of the patient(M/F): '))
Main.Age()
while(Stop == False):    
    KEYS = input('Enter method: ')
    if KEYS == 'stop':
        Stop = True
    else:
        Main.ChooseMethods(KEYS)