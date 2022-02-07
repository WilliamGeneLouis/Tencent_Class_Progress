text = "gfmncwmsbgblrrpylqjyrcgrzwfylb.rfyrqufyramknsrcpqypcdmp.bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(ord('a'))

for element in text:

	if element >= 'a' and element <= 'z':
		element = chr ((ord(element) - ord('a') + 2 ) % 26 + ord('a'))
		print(element, end='')

	else:
		print(element, end='')

print('\n')

print(''.join( [chr ((ord(element) - ord('a') + 2 ) % 26 + ord('a')) if 'a' <= element <= 'z' else element for element in text]) )

