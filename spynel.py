

















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































#vaza daqui yag



import base64

sai_daqui = b'CmZyb20gcmVxdWVzdHMgaW1wb3J0IGdldApmcm9tIG9zIGltcG9ydCBzeXN0ZW0sIGV4ZWN2CmZyb20gc3lzIGltcG9ydCBhcmd2LCBleGVjdXRhYmxlCmZyb20gcmFuZG9tIGltcG9ydCBjaG9pY2UKCmYgPSAnG1ttJwp2ZXJtZWxobyA9ICcbWzMxbScKdiA9ICcbWzkyOzFtJwphbWFyZWxvID0gJxtbMzNtJwphenVsID0gJxtbMzRtJwpyb3hvID0gJxtbMzVtJwpiID0gJxtbMW0nCgpkZWYgY2xlYXIoKToKCXN5c3RlbSgnY2xzfHxjbGVhcicpCmRlZiByZXN0YXJ0KCk6CglleGVjdihleGVjdXRhYmxlLCBbJ3B5dGhvbjMnXSArIGFyZ3YpCmRlZiBiYW5lcigpOgoJc3lzdGVtKCdjYXQgYmFubmVyIHwgbG9sY2F0JykKZGVmIGVudCgpOgoJaW5wdXQoJycnCmVudGVyIHBhcmEgY29udGludWFyJycnKQpkZWYgY3JkKCk6CglwcmludChmJ2J5OiAbWzk0OzE7NG1TcHl3YXJle2Z9JykKCmNsZWFyKCkKYmFuZXIoKQpjcmQoKQpjb3JlcyA9IFsnG1s5MTsxbScsICcbWzkyOzFtJywgJxtbOTM7MW0nLCAnG1s5NDsxbScsICcbWzk1OzFtJywgJxtbOTY7MW0nXQpjb3IgPSBjaG9pY2UoY29yZXMpCnRyeToKCW9wYyA9IGlucHV0KGYnJyd7Yn3in6p7Zn0ge2Nvcn0xe2Z9IHtifeKfqyA+e2Z9IHtjb3J9SVB7Zn0gKHt2fU9Oe2Z9KQp7Yn3in6p7Zn0ge2Nvcn0ye2Z9IHtifeKfqyA+e2Z9IHtjb3J9Q0VQe2Z9ICh7dn1PTntmfSkKe2J94p+qe2Z9IHtjb3J9M3tmfSB7Yn3in6sgPntmfSB7Y29yfVBMQUNBIERFIENBUlJPe2Z9ICh7dn1PTntmfSkKe2J94p+qe2Z9IHtjb3J9NHtmfSB7Yn3in6sgPntmfSB7Y29yfUNOUEp7Zn0gKHt2fU9Oe2Z9KSh7dn1FTSBURVNURXtmfSkKCntifeKfqntmfSB7Y29yfTB7Zn0ge2J94p+rID57Zn0ge2Nvcn1TQUlSe2Z9CntifeKfqntmfSB7Y29yfTk5e2Z9IHtifeKfqyA+e2Z9IHtjb3J9QVRVQUxJWkFSe2Z9Cgp7Yn0+Pj57Zn0gJycnKS5zdHJpcCgpCmV4Y2VwdDoKCXJlc3RhcnQoKQppZiBvcGMgPT0gJyc6CglyZXN0YXJ0KCkKCmlmIG9wY1swXSA9PSAnMSc6Cgl3aGlsZSBUcnVlOgoJCWNsZWFyKCkKCQljcmQoKQoJCW9wYyA9IGlucHV0KGYnJyd7Yn1be2Z9IHtjb3J9MXtmfSB7Yn1dID57Zn0ge2Nvcn1JUCAxe2Z9CntifVt7Zn0ge2Nvcn0ye2Z9IHtifV0gPntmfSB7Y29yfUlQIDJ7Zn0Ke2J9W3tmfSB7Y29yfTN7Zn0ge2J9XSA+e2Z9IHtjb3J9TUVVIElQe2Z9Cgp7Yn1be2Z9IHtjb3J9MHtmfSB7Yn1dID57Zn0ge2Nvcn1TQUlSe2Z9Cgp7Yn0+Pj57Zn0gJycnKS5zdHJpcCgpWzBdCgkJaWYgb3BjID09ICcxJzoKCQkJaXAgPSBpbnB1dCgnSVA6ICcpLnN0cmlwKCkKCQkJZGEgPSBnZXQoZidodHRwczovL2lwaW5mby5pby97aXB9L2pzb24nKS5qc29uKCkKCQkJZm9yIGMgaW4gZGE6CgkJCQlpZiBjICE9ICdyZWFkbWUnIGFuZCBkYVtjXSAhPSAnJzoKCQkJCQlwcmludChmJ3t2fXtjfTp7Zn0ge2J9e2RhW2NdfXtmfScpCgkJZWxpZiBvcGMgPT0gJzInOgoJCQlpcCA9IGlucHV0KCdJUDogJykuc3RyaXAoKQoJCQlkYSA9IGdldChmJ2h0dHBzOi8vYXBpLmlwZmluZC5jb20vP2lwPXtpcH0nKS5qc29uKCkKCQkJZm9yIGMgaW4gZGE6CgkJCQlpZiBjICE9ICd3YXJuaW5nJyBhbmQgZGFbY10gIT0gJyc6CgkJCQkJcHJpbnQoZid7dn17Y306e2Z9IHtifXtkYVtjXX17Zn0nKQoJCWVsaWYgb3BjID09ICczJzoKCQkJaXAgPSBnZXQoZidodHRwczovL2lwaW5mby5pby93aGF0LWlzLW15LWlwJykuanNvbigpCgkJCWZvciBpIGluIGlwOgoJCQkJaWYgaSAhPSAncmVhZG1lJyBhbmQgaXBbaV0gIT0gJyc6CgkJCQkJcHJpbnQoZid7dn17aX06e2Z9IHtifXtpcFtpXX17Zn0nKQoJCWVsaWYgb3BjID09ICcwJzoKCQkJcmVzdGFydCgpCgkJZW50KCkKCmVsaWYgb3BjWzBdID09ICcyJzoKCXdoaWxlIFRydWU6CgkJY2xlYXIoKQoJCWNyZCgpCgkJb3BjID0gaW5wdXQoZicnJ3tifVt7Zn0ge2Nvcn0xe2Z9IHtifV0gPntmfSB7Y29yfUNFUCAxe2Z9CntifVt7Zn0ge2Nvcn0ye2Z9IHtifV0gPntmfSB7Y29yfUNFUCAye2Z9Cgp7Yn1be2Z9IHtjb3J9MHtmfSB7Yn1dID57Zn0ge2Nvcn1TQUlSe2Z9Cgp7Yn0+Pj57Zn0gJycnKS5zdHJpcCgpWzBdCgkJaWYgb3BjID09ICcxJzoKCQkJY2VwID0gaW5wdXQoZicnJ3tifWV4OntmfSA2NTY5NTAwMApDRVA6ICcnJykuc3RyaXAoKQoJCQlkID0gZ2V0KGYnaHR0cHM6Ly92aWFjZXAuY29tLmJyL3dzL3tjZXB9L2pzb24nKS5qc29uKCkKCQkJZm9yIGMgaW4gZDoKCQkJCWlmIGRbY10gIT0gJyc6CgkJCQkJcHJpbnQoZid7dn17Y306e2Z9IHtifXtkW2NdfXtmfScpCgkJZWxpZiBvcGMgPT0gJzInOgoJCQljZXAgPSBpbnB1dChmJycne2J9ZXg6e2Z9IDY1Njk1MDAwCkNFUDogJycnKS5zdHJpcCgpCgkJCWQgPSBnZXQoZidodHRwczovL3RyaWFsLmFwaS5maW5kY2VwLmNvbS92MS9jZXAve2NlcH0uanNvbicpLmpzb24oKQoJCQlmb3IgaSBpbiBkOgoJCQkJaWYgZFtpXSAhPSAnJzoKCQkJCQlwcmludChmJ3t2fXtpfTp7Zn0ge2J9e2RbaV19e2Z9JykKCQllbGlmIG9wYyA9PSAnMCc6CgkJCXJlc3RhcnQoKQoJCWVudCgpCgplbGlmIG9wY1swXSA9PSAnMyc6CglwbGMgPSBpbnB1dChmJycne2J9ZXg6e2Z9IEFUSjg2MTcKUExBQ0E6ICcnJykuc3RyaXAoKS51cHBlcigpCglyID0gZ2V0KGYnaHR0cHM6Ly9hcGljYXJyb3MuY29tL3YxL2NvbnN1bHRhL3twbGN9L2pzb24nLCB2ZXJpZnk9RmFsc2UpLmpzb24oKQoJYyA9IDAKCWZvciBpIGluIHI6CgkJaWYgYyA9PSAwOiBjbGVhcigpOyBjcmQoKQoJCWlmIHJbaV0gIT0gJyc6CgkJCXByaW50KGYne3Z9e2l9OntmfSB7Yn17cltpXX17Zn0nKQoJCWMgKz0gMQoJZW50KCkKCmVsaWYgb3BjWzBdID09ICc0JzoKCWNucGogPSBpbnB1dChmJycne2J9ZXg6e2Z9IDAzNzc4MTMwMDAwMTQ4CkNOUEo6ICcnJykuc3RyaXAoKQoJZGEgPSBnZXQoZidodHRwczovL3d3dy5yZWNlaXRhd3MuY29tLmJyL3YxL2NucGove2NucGp9LycpLmpzb24oKQoJZm9yIGkgaW4gZGE6CgkJaWYgZGFbaV0gIT0gJyc6CgkJCWlmIHR5cGUoZGFbaV0pID09IHN0ciBvciBpbnQ6CgkJCQlwcmludChmJ3t2fXtpfTp7Zn0ge2J9e2RhW2ldfXtmfScpCgljcmQoKQoJZW50KCkKCmVsaWYgb3BjWzBdID09ICcwJzoKCWNsZWFyKCkKCXByaW50KGYnJyd7dn1PYnJpZ2FkbyBwb3IgdXNhciBvIG1ldSBwYWluZWwhCkRlaXhlIHN1YSBlc3RyZWxhIG5vIGdpdGh1YiBlIHZvbHRlIHNlbXByZSA6KXtmfScnJykKCWV4aXQoKQoKZWxpZiBvcGNbOjJdID09ICc5OSc6CglzeXN0ZW0oJycnbXYgYS5zaCAkSE9NRSAmJiBjZCAmJiBiYXNoIGEuc2gnJycpCgplbHNlOgoJcmVzdGFydCgpCgpyZXN0YXJ0KCkKCg=='
exec(base64.b64decode(sai_daqui))
