import qrcode

#1 generate_qrcode 함수
def generate_qrcode(data, static_dir):
    static_dir.mkdir(parents=True, exist_ok=True)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    #2 static 폴더에 qrcode.png 저장
    img.save(static_dir / 'qrcode.png')
