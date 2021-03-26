import dropbox
class TransferData:
    def __init__(self,access_token):
            self.access_token = access_token
    def upload_file(self,file_from,file_to):
            dbx = dropbox.Dropbox(self.access_token)

            f = open(file_from,'rb')   
            dbx.files_upload(f.read(),file_to)

def main():
        access_token = 'sl.Ar_uoY9gGR62oLmVZiEkJGrRnAQzidbVlnTDsr60hCQ0NEhmDJynY8szJrzd2u8yvQVcD5Va59Ez1ni_MqM8EBhbRvkkSz5q-RBnvdnKuXmsB6dfEOV7fjrUiOxbB363dJc7oRM'
        transferData = TransferData(access_token)

        file_from = input("Enter the file path to transfer")
        file_to = input("Enter the full path to upload to dropbox")

        transferData.upload_file(file_from,file_to)
        print("file has been moved")

main()