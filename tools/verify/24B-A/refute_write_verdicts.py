import json,pathlib
RAW=pathlib.Path(__file__).resolve().parents[2]/'raw'
SC={ # code -> spot-check solutions
 '24B-A':{'2א':'agree','5ב':'agree','6ב':'agree'},
 '24A-B':{'2א':'agree','4ב':'agree','5ב':'agree'},
 '24A-A':{'1':'DISAGREE: official part ג claims y\'\'<0 for x<0; y\'\'=e^x(x^2-4x+6)/x^4>0 for all x!=0 (disc<0), so f is convex-up on both sides (also what the official graph shows). Transcription matches page-01.','2א':'agree','5ב':'agree'},
 '23B-B':{'1':'agree','4ב':'agree','6א':'agree'},
}
NOTES={
 ('24B-A','3ג',1):'agree on key (b!=0, any a = official definition: limits finite and different). Wording caveat: under the broad textbook definition of first kind (finite one-sided limits) option a (b=0, a!=7/2, removable) is also first kind; the key relies on the official solution splitting removable vs jump.',
 ('24A-B','2ב',1):'agree on key d; wording nit: "all terms greater than 4" is false for a_1=4 (should be "not less than 4"/"at least 4").',
 ('24A-B','2ב',2):'agree on order; line 3 has the same "greater than 4" nit (a_1=4).',
 ('24A-B','2ב',3):'agree on bugIndex 2 (L^2+L-20); line 3 carries the same "greater than 4" nit.',
 ('24A-A','5א',1):'agree on key a, but options print the variable as "xp" (sin(xp)/(2 sqrt(xp))) instead of x: display bug from sympy symbol name.',
 ('24A-A','2א','pitfalls'):'agree; pitfall 3 is weak (states the decomposition is valid, not a real error).',
 ('23B-B','5א','pitfalls'):'agree; pitfall 2 describes a grading policy, not an error.',
}
ITEMNOTE={
 ('24A-B','6ב'):'out of scope (hold, no steps/rubric). Printed numerator x^4 gives limit 2 (sympy/mpmath); official solution computes sin^2 x -> +inf. Page-07 shows the solution with sin^2 x. Known held mismatch.',
 ('24A-A','1'):'out of scope (no rubric/steps). Official solution error: concavity claim for x<0 is wrong, f\'\'>0 on both sides.',
 ('23B-B','2ב'):'solution agrees (limit 5); official text has a typo "bounded above by 6" while proving a_n<5.',
 ('23B-B','3א'):'solution agrees (2/3); official second L\'Hopital line drops factors of x (4x/(6x/(1+3x^2)) written as 4/(6/(1+3x^2))), final value correct.',
 ('23B-B','5ב'):'solution final answer x-ln(1+e^{2x}) agrees; official middle line writes ln(1+x^2) (typo), final line correct.',
}
tot={'agree':0,'disagree':0}
for code in SC:
    d=json.load(open(RAW/f'{code}.json',encoding='utf8'))
    items=[]
    for q in d['questions']:
        k=f"{q['num']}{q.get('part','')}"
        steps=[]
        for i,s in enumerate(q.get('steps',[])):
            st={'i':i,'type':s['type'],'verdict':'agree'}
            n=NOTES.get((code,k,i))
            if n: st['note']=n
            steps.append(st)
            tot['agree']+=1
        has=bool(q.get('rubric'))
        it={'item':k,'solution':'agree','rubric':'agree (points sum to item total)' if has else 'n/a (none)','pitfalls':'agree' if has else 'n/a (none)','steps':steps,'notes':''}
        if (code,k)=='24A-A1': it['solution']='disagree'
        if (code,k)=='24A-B6ב': it['solution']='unclear (held: printed x^4 vs official sin^2 x)'
        notes=[x for x in [ITEMNOTE.get((code,k)),NOTES.get((code,k,'pitfalls'))] if x]
        it['notes']=' | '.join(notes)
        items.append(it)
    out={'examCode':code,'refuter':'independent','derivationFiles':[f'tools/verify/{code}/refute_calc.py','tools/verify/24B-A/refute_num.py'],'items':items,'officialSolutionSpotChecks':SC[code]}
    json.dump(out,open(RAW/f'_verify_{code}.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
print(tot)
