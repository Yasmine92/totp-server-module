# totp-server-module
Time-based One-time Password Python module for server side

##Steps


###Step1:key Genaration

we generate the key that could be added to the TOTP mobile app, via base32, or QR code

```sh
[root@yasmine]# python generate_key.py
Generated key in ascii==> c?ednAbHNeP:OdlowJUr
Generated key in hex==> 633f65646e4162484e65503a4f646c6f774a5572
Generated key in base32==> MM7WKZDOIFREQTTFKA5E6ZDMN53UUVLS
google_auth_qr==>https://chart.googleapis.com/chart?chs=166x166&chld=L|0&cht=qr&chl=otpauth://totp/new%20secret%20key%3Fsecret=MM7WKZDOIFREQTTFKA5E6ZDMN53UUVLS
```


###Step1:Generated code testing

we test that the generated code by the mobile app is approved by the TOTP server, using this module 
```sh
[root@yasmine]#python validate_generated_totp.py
Enter your key and code value: MM7WKZDOIFREQTTFKA5E6ZDMN53UUVLS 430257
MM7WKZDOIFREQTTFKA5E6ZDMN53UUVLS
430257
your code is correct
```
