#Cracking Caesar Cipher Frequency Analysis by Hajiahmad Ahmadzada

def dictionary_maker(encrypted_string):
    stored_letters = {}
    encrypted_string.upper()
    for char in encrypted_string:
        if char not in stored_letters:
            stored_letters[char] = 1
        else:
            stored_letters[char] += 1

    return stored_letters

encrypted_string = input("""
----------------------------------
Please enter your encrypted string
----------------------------------

=> """)

#Example like this
#cpf = the
#u = o
#q = n

attempt = encrypted_string.replace("C","\033[31mT\033[0m")
attempt = attempt.replace("P","\033[31mH\033[0m")
attempt = attempt.replace("F","\033[31mE\033[0m")
attempt = attempt.replace("U","\033[31mO\033[0m")
attempt = attempt.replace("Q","\033[31mN\033[0m")

print(attempt)
#print(dictionary_maker(encrypted_string))
#In line 40, we return dictionary.

#The given plaintext
"""It so happened that the little Delaneys spent the greater part of their time in a beautiful garden. I don't think, in all the course of my wanderings, I ever saw a garden quite to compare to that in which their early days were spent. Even in the winter they lived the greater part of their time here, being hardy children and never catching cold. The house was a fine and beautiful building, having belonged to their family for several generations, but the children thought nothing at all of that in comparison with the garden. Here, when possible, they even had their lessons; here they played all their wonderful and remarkable games; here they went through their brief sorrows, and tasted their sweetest joys. But I must hasten to describe the garden itself. In the first place, it was old-fashioned, having very high brick walls covered all over with fruit trees. These fruit trees had grown slowly, and were now in the perfection of their prime. Never were such peaches to be seen, nor such apricots, nor such cherries, as ripened slowly on the red brick walls of the old garden. Inside the walls almost all well-known English flowers flourished in lavish profusion. There was also fruit to be found here in quantities. Never were such strawberries to be seen as could be gathered from those great strawberry beds. Then the gooseberries with which the old bushes were laden; the currants, red, black, and white; the raspberries, had surely their match nowhere else on this earth. The walled-in garden contained quite five acres of ground, and was divided itself into three portions. In the middle was the flower garden proper. Here there was a long, straight walk which led to an arbor at the bottom. The children were particularly fond of this arbor, for their father had made it for them with his own hands, and their mother had watched its growth. Mrs. Delaney was very delicate at the time, and as she looked on and saw the pretty arbor growing into shape, she used to lean on Iris' arm and talk to her now and then in her soft, low voice about the flowers and the animals, and the happy life which the little people were leading. At these moments a look would often come into her mother's gentle eyes which caused Iris' heart to beat fast, and made her tighten her clasp on the slender arm. Then, when the arbor was quite finished, Mr. Delaney put little seats into it, a rustic chair for each child, which he or she could take in or out at pleasure. The chairs were carved in commemoration of each child's name. Iris had the deep purple flowers which go by that name twined round and round the back of hers. Apollo's chair was made memorable with his well-known lyre and bow, and these words were carved round it: "The golden lyre shall be my friend, the bent bow my delight, and in oracles will I foretell the dark future."""

#The secret encrypted cipher
"""KV UQ JCRRGPGF VJCV VJG NKVVNG FGNCPGAU URGPV VJG ITGCVGT RCTV QH VJGKT VKOG KP C DGCWVKHWN ICTFGP. K FQP'V VJKPM, KP CNN VJG EQWTUG QH OA YCPFGTKPIU, K GXGT UCY C ICTFGP SWKVG VQ EQORCTG VQ VJCV KP YJKEJ VJGKT GCTNA FCAU YGTG URGPV. GXGP KP VJG YKPVGT VJGA NKXGF VJG ITGCVGT RCTV QH VJGKT VKOG JGTG, DGKPI JCTFA EJKNFTGP CPF PGXGT ECVEJKPI EQNF. VJG JQWUG YCU C HKPG CPF DGCWVKHWN DWKNFKPI, JCXKPI DGNQPIGF VQ VJGKT HCOKNA HQT UGXGTCN IGPGTCVKQPU, DWV VJG EJKNFTGP VJQWIJV PQVJKPI CV CNN QH VJCV KP EQORCTKUQP YKVJ VJG ICTFGP. JGTG, YJGP RQUUKDNG, VJGA GXGP JCF VJGKT NGUUQPU; JGTG VJGA RNCAGF CNN VJGKT YQPFGTHWN CPF TGOCTMCDNG ICOGU; JGTG VJGA YGPV VJTQWIJ VJGKT DTKGH UQTTQYU, CPF VCUVGF VJGKT UYGGVGUV LQAU. DWV K OWUV JCUVGP VQ FGUETKDG VJG ICTFGP KVUGNH. KP VJG HKTUV RNCEG, KV YCU QNF-HCUJKQPGF, JCXKPI XGTA JKIJ DTKEM YCNNU EQXGTGF CNN QXGT YKVJ HTWKV VTGGU. VJGUG HTWKV VTGGU JCF ITQYP UNQYNA, CPF YGTG PQY KP VJG RGTHGEVKQP QH VJGKT RTKOG. PGXGT YGTG UWEJ RGCEJGU VQ DG UGGP, PQT UWEJ CRTKEQVU, PQT UWEJ EJGTTKGU, CU TKRGPGF UNQYNA QP VJG TGF DTKEM YCNNU QH VJG QNF ICTFGP. KPUKFG VJG YCNNU CNOQUV CNN YGNN-MPQYP GPINKUJ HNQYGTU HNQWTKUJGF KP NCXKUJ RTQHWUKQP. VJGTG YCU CNUQ HTWKV VQ DG HQWPF JGTG KP SWCPVKVKGU. PGXGT YGTG UWEJ UVTCYDGTTKGU VQ DG UGGP CU EQWNF DG ICVJGTGF HTQO VJQUG ITGCV UVTCYDGTTA DGFU. VJGP VJG IQQUGDGTTKGU YKVJ YJKEJ VJG QNF DWUJGU YGTG NCFGP; VJG EWTTCPVU, TGF, DNCEM, CPF YJKVG; VJG TCURDGTTKGU, JCF UWTGNA VJGKT OCVEJ PQYJGTG GNUG QP VJKU GCTVJ. VJG YCNNGF-KP ICTFGP EQPVCKPGF SWKVG HKXG CETGU QH ITQWPF, CPF YCU FKXKFGF KVUGNH KPVQ VJTGG RQTVKQPU. KP VJG OKFFNG YCU VJG HNQYGT ICTFGP RTQRGT. JGTG VJGTG YCU C NQPI, UVTCKIJV YCNM YJKEJ NGF VQ CP CTDQT CV VJG DQVVQO. VJG EJKNFTGP YGTG RCTVKEWNCTNA HQPF QH VJKU CTDQT, HQT VJGKT HCVJGT JCF OCFG KV HQT VJGO YKVJ JKU QYP JCPFU, CPF VJGKT OQVJGT JCF YCVEJGF KVU ITQYVJ. OTU. FGNCPGA YCU XGTA FGNKECVG CV VJG VKOG, CPF CU UJG NQQMGF QP CPF UCY VJG RTGVVA CTDQT ITQYKPI KPVQ UJCRG, UJG WUGF VQ NGCP QP KTKU' CTO CPF VCNM VQ JGT PQY CPF VJGP KP JGT UQHV, NQY XQKEG CDQWV VJG HNQYGTU CPF VJG CPKOCNU, CPF VJG JCRRA NKHG YJKEJ VJG NKVVNG RGQRNG YGTG NGCFKPI. CV VJGUG OQOGPVU C NQQM YQWNF QHVGP EQOG KPVQ JGT OQVJGT'U IGPVNG GAGU YJKEJ ECWUGF KTKU' JGCTV VQ DGCV HCUV, CPF OCFG JGT VKIJVGP JGT ENCUR QP VJG UNGPFGT CTO. VJGP, YJGP VJG CTDQT YCU SWKVG HKPKUJGF, OT. FGNCPGA RWV NKVVNG UGCVU KPVQ KV, C TWUVKE EJCKT HQT GCEJ EJKNF, YJKEJ JG QT UJG EQWNF VCMG KP QT QWV CV RNGCUWTG. VJG EJCKTU YGTG ECTXGF KP EQOOGOQTCVKQP QH GCEJ EJKNF'U PCOG. KTKU JCF VJG FGGR RWTRNG HNQYGTU YJKEJ IQ DA VJCV PCOG VYKPGF TQWPF CPF TQWPF VJG DCEM QH JGTU. CRQNNQ'U EJCKT YCU OCFG OGOQTCDNG YKVJ JKU YGNN-MPQYP NATG CPF DQY, CPF VJGUG YQTFU YGTG ECTXGF TQWPF KV: "VJG IQNFGP NATG UJCNN DG OA HTKGPF, VJG DGPV DQY OA FGNKIJV, CPF KP QTCENGU YKNN K HQTGVGNN VJG FCTM HWVWTG."""
