import unittest

import iocextract

# Helper functions
def _wrap_spaces(content):
    return '  {c}  '.format(c=content)

def _wrap_tabs(content):
    return '\t\t{c}\t\t'.format(c=content)

def _wrap_newlines(content):
    return '\r\n{c}\r\n'.format(c=content)

def _wrap_words(content):
    return 'words{c}words'.format(c=content)

def _wrap_nonwords(content):
    return '.!@..{c}!@#-'.format(c=content)


# Tests
class TestExtractors(unittest.TestCase):

    def test_corpus_results(self):
        in_data = open('test_data/input.txt', 'r').read()
        valid_results = open('test_data/valid.txt', 'r').read().splitlines()
        invalid_results = open('test_data/invalid.txt', 'r').read().splitlines()

        out_data = list(iocextract.extract_iocs(in_data))

        for expected in valid_results:
            self.assertIn(expected, out_data)

        for unexpected in invalid_results:
            self.assertNotIn(unexpected, out_data)

    def test_md5_extract(self):
        content = '68b329da9893e34099c7d8ad5cb9c940'

        self.assertEquals(list(iocextract.extract_md5_hashes(content))[0], content)
        self.assertEquals(list(iocextract.extract_md5_hashes(_wrap_spaces(content)))[0], content)
        self.assertEquals(list(iocextract.extract_md5_hashes(_wrap_tabs(content)))[0], content)
        self.assertEquals(list(iocextract.extract_md5_hashes(_wrap_newlines(content)))[0], content)
        self.assertEquals(list(iocextract.extract_md5_hashes(_wrap_words(content)))[0], content)
        self.assertEquals(list(iocextract.extract_md5_hashes(_wrap_nonwords(content)))[0], content)

    def test_sha1_extract(self):
        content = 'adc83b19e793491b1c6ea0fd8b46cd9f32e592fc'

        self.assertEquals(list(iocextract.extract_sha1_hashes(content))[0], content)
        self.assertEquals(list(iocextract.extract_sha1_hashes(_wrap_spaces(content)))[0], content)
        self.assertEquals(list(iocextract.extract_sha1_hashes(_wrap_tabs(content)))[0], content)
        self.assertEquals(list(iocextract.extract_sha1_hashes(_wrap_newlines(content)))[0], content)
        self.assertEquals(list(iocextract.extract_sha1_hashes(_wrap_words(content)))[0], content)
        self.assertEquals(list(iocextract.extract_sha1_hashes(_wrap_nonwords(content)))[0], content)

    def test_sha256_extract(self):
        content = '01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b'

        self.assertEquals(list(iocextract.extract_sha256_hashes(content))[0], content)
        self.assertEquals(list(iocextract.extract_sha256_hashes(_wrap_spaces(content)))[0], content)
        self.assertEquals(list(iocextract.extract_sha256_hashes(_wrap_tabs(content)))[0], content)
        self.assertEquals(list(iocextract.extract_sha256_hashes(_wrap_newlines(content)))[0], content)
        self.assertEquals(list(iocextract.extract_sha256_hashes(_wrap_words(content)))[0], content)
        self.assertEquals(list(iocextract.extract_sha256_hashes(_wrap_nonwords(content)))[0], content)

    def test_sha512_extract(self):
        content = 'be688838ca8686e5c90689bf2ab585cef1137c999b48c70b92f67a5c34dc15697b5d11c982ed6d71be1e1e7f7b4e0733884aa97c3f7a339a8ed03577cf74be09'

        self.assertEquals(list(iocextract.extract_sha512_hashes(content))[0], content)
        self.assertEquals(list(iocextract.extract_sha512_hashes(_wrap_spaces(content)))[0], content)
        self.assertEquals(list(iocextract.extract_sha512_hashes(_wrap_tabs(content)))[0], content)
        self.assertEquals(list(iocextract.extract_sha512_hashes(_wrap_newlines(content)))[0], content)
        self.assertEquals(list(iocextract.extract_sha512_hashes(_wrap_words(content)))[0], content)
        self.assertEquals(list(iocextract.extract_sha512_hashes(_wrap_nonwords(content)))[0], content)

    def test_md5_not_in_shax(self):
        content = 'adc83b19e793491b1c6ea0fd8b46cd9f32e592fc'

        self.assertEquals(len(list(iocextract.extract_md5_hashes(content))), 0)
        self.assertEquals(len(list(iocextract.extract_md5_hashes(_wrap_spaces(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_md5_hashes(_wrap_tabs(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_md5_hashes(_wrap_newlines(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_md5_hashes(_wrap_words(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_md5_hashes(_wrap_nonwords(content)))), 0)

        content = '01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b'

        self.assertEquals(len(list(iocextract.extract_md5_hashes(content))), 0)
        self.assertEquals(len(list(iocextract.extract_md5_hashes(_wrap_spaces(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_md5_hashes(_wrap_tabs(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_md5_hashes(_wrap_newlines(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_md5_hashes(_wrap_words(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_md5_hashes(_wrap_nonwords(content)))), 0)

        content = 'be688838ca8686e5c90689bf2ab585cef1137c999b48c70b92f67a5c34dc15697b5d11c982ed6d71be1e1e7f7b4e0733884aa97c3f7a339a8ed03577cf74be09'

        self.assertEquals(len(list(iocextract.extract_md5_hashes(content))), 0)
        self.assertEquals(len(list(iocextract.extract_md5_hashes(_wrap_spaces(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_md5_hashes(_wrap_tabs(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_md5_hashes(_wrap_newlines(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_md5_hashes(_wrap_words(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_md5_hashes(_wrap_nonwords(content)))), 0)

    def test_sha1_not_in_shaxxx(self):
        content = '01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b'

        self.assertEquals(len(list(iocextract.extract_sha1_hashes(content))), 0)
        self.assertEquals(len(list(iocextract.extract_sha1_hashes(_wrap_spaces(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_sha1_hashes(_wrap_tabs(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_sha1_hashes(_wrap_newlines(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_sha1_hashes(_wrap_words(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_sha1_hashes(_wrap_nonwords(content)))), 0)

        content = 'be688838ca8686e5c90689bf2ab585cef1137c999b48c70b92f67a5c34dc15697b5d11c982ed6d71be1e1e7f7b4e0733884aa97c3f7a339a8ed03577cf74be09'

        self.assertEquals(len(list(iocextract.extract_sha1_hashes(content))), 0)
        self.assertEquals(len(list(iocextract.extract_sha1_hashes(_wrap_spaces(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_sha1_hashes(_wrap_tabs(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_sha1_hashes(_wrap_newlines(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_sha1_hashes(_wrap_words(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_sha1_hashes(_wrap_nonwords(content)))), 0)

    def test_sha256_not_in_sha512(self):
        content = 'be688838ca8686e5c90689bf2ab585cef1137c999b48c70b92f67a5c34dc15697b5d11c982ed6d71be1e1e7f7b4e0733884aa97c3f7a339a8ed03577cf74be09'

        self.assertEquals(len(list(iocextract.extract_sha256_hashes(content))), 0)
        self.assertEquals(len(list(iocextract.extract_sha256_hashes(_wrap_spaces(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_sha256_hashes(_wrap_tabs(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_sha256_hashes(_wrap_newlines(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_sha256_hashes(_wrap_words(content)))), 0)
        self.assertEquals(len(list(iocextract.extract_sha256_hashes(_wrap_nonwords(content)))), 0)

    def test_hash_extract(self):
        content = """
            68b329da9893e34099c7d8ad5cb9c940
            adc83b19e793491b1c6ea0fd8b46cd9f32e592fc
            01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b
            be688838ca8686e5c90689bf2ab585cef1137c999b48c70b92f67a5c34dc15697b5d11c982ed6d71be1e1e7f7b4e0733884aa97c3f7a339a8ed03577cf74be09
        """

        processed = list(iocextract.extract_hashes(content))

        self.assertEquals(len(processed), 4)
        self.assertEquals(processed[0], '68b329da9893e34099c7d8ad5cb9c940')

        processed = list(iocextract.extract_iocs(content))

        self.assertEquals(len(processed), 4)
        self.assertEquals(processed[0], '68b329da9893e34099c7d8ad5cb9c940')
