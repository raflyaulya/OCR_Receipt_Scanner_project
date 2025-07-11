
lis_invoicePict = []

name_invoicePict = 'invoice'

for i in range(9):
    # ==========    print('invoice', str(i+1))   =================
    # print('invoice', end='')
    # print(str(i+1), end='')
    # print('.jpg')
    # invoice_pict/invoice3.jpg

    nameUnited_invoicePict = 'invoice_pict/invoice' + str(i +1) + '.jpg'
    lis_invoicePict.append(nameUnited_invoicePict)

    # lis_invoicePict.append('invoice', str(i+1), '.jpg')

print(str(lis_invoicePict))