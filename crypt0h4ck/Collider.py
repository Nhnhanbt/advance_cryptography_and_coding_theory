import hashlib
from utils import listener


FLAG = "crypto{???????????????????????????????????}"


class Challenge():
    def __init__(self):
        self.before_input = "Give me a document to store\n"
        self.documents = {
            "508dcc4dbe9113b15a1f971639b335bd": b"Particle physics (also known as high energy physics) is a branch of physics that studies the nature of the particles that constitute matter and radiation. Although the word particle can refer to various types of very small objects (e.g. protons, gas particles, or even household dust), particle physics usually investigates the irreducibly smallest detectable particles and the fundamental interactions necessary to explain their behaviour.",
            "cb07ff7a5f043361b698c31046b8b0ab": b"The Large Hadron Collider (LHC) is the world's largest and highest-energy particle collider and the largest machine in the world. It was built by the European Organization for Nuclear Research (CERN) between 1998 and 2008 in collaboration with over 10,000 scientists and hundreds of universities and laboratories, as well as more than 100 countries.",
        }

    def challenge(self, msg):
        if "document" not in msg:
            self.exit = True
            return {"error": "You must send a document"}

        document = bytes.fromhex(msg["document"])
        document_hash = hashlib.md5(document).hexdigest()

        if document_hash in self.documents.keys():
            self.exit = True
            if self.documents[document_hash] == document:
                return {"error": "Document already exists in system"}
            else:
                return {"error": f"Document system crash, leaking flag: {FLAG}"}

        self.documents[document_hash] = document

        if len(self.documents) > 5:
            self.exit = True
            return {"error": "Too many documents in the system"}

        return {"success": f"Document {document_hash} added to system"}


import builtins; builtins.Challenge = Challenge # hack to enable challenge to be run locally, see https://cryptohack.org/faq/#listener
"""
When you connect, the 'challenge' function will be called on your JSON
input.
"""
listener.start_server(port=13389)
##############################################################################
# Write up for this challenge

# This Challenge receive a JSON format as it input: 

# {"document":"content_of_document"}

# Then the server will calculate the MD5 hash value, store and check with stored content. 
# We will get the flag when collision occur. 
# => Look for example MD5 collision pair on the internet.
# https://stackoverflow.com/questions/933497/create-your-own-md5-collisions

# telnet socket.cryptohack.org 13389
# Trying 134.122.111.232...
# Connected to socket.cryptohack.org.
# Escape character is '^]'.
# Give me a document to store
# {"document":"d131dd02c5e6eec4693d9a0698aff95c 2fcab58712467eab4004583eb8fb7f89  55ad340609f4b30283e488832571415a 085125e8f7cdc99fd91dbdf280373c5b  d8823e3156348f5bae6dacd436c919c6 dd53e2b487da03fd02396306d248cda0  e99f33420f577ee8ce54b67080a80d1e c69821bcb6a8839396f9652b6ff72a70"}
# {"success": "Document 79054025255fb1a26e4bc422aef54eb4 added to system"}
# {"document":"d131dd02c5e6eec4693d9a0698aff95c 2fcab50712467eab4004583eb8fb7f89  55ad340609f4b30283e4888325f1415a 085125e8f7cdc99fd91dbd7280373c5b  d8823e3156348f5bae6dacd436c919c6 dd53e23487da03fd02396306d248cda0  e99f33420f577ee8ce54b67080280d1e c69821bcb6a8839396f965ab6ff72a70"}
# {"error": "Document system crash, leaking flag: crypto{m0re_th4n_ju5t_p1g30nh0le_pr1nc1ple}"}
# Connection closed by foreign host.
