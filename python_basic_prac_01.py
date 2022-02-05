'''text = "gfmncwmsbgblrrpylqjyrcgrzwfylb.rfyrqufyramknsrcpqypcdmp.bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

index = 0

while index < len(text):

    print(text[index], end='')

    if text[index] == 'k':
        text[index] == 'm'
        index += 1

    elif text[index] == 'o':
        text[index] == 'q'
        index += 1

    elif text[index] == 'e':
        text[index] == 'g'
        index += 1

    else:
        index +=1

else:
    print('not found')


b_list = list('asdasda')

index = 0

while index < len(b_list):

    if b_list[index] == 'a':
        print(index)

        b_list[index] == 'g'            # 此时替换不起作用
        print(b_list[index])

        index +=1
        print(index)

    else:
        print(b_list[index], end='')
        index +=1

else:
    print('none')

'''

