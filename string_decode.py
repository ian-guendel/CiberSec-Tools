import base64

bytes_decoded = base64.b64decode("""
                                    SQBFAFgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkAL
                                    gBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAiAGgAdAB0AHAAcwA6AC8ALwByAGEAdwAuAGcAaQB0AGgAdQ
                                    BiAHUAcwBlAHIAYwBvAG4AdABlAG4AdAAuAGMAbwBtAC8AQgBDAC0AUwBFAEMAVQBSAEkAVABZAC8ARQBtAHAAaQBy
                                    AGUALwBtAGEAcwB0AGUAcgAvAGQAYQB0AGEALwBtAG8AZAB1AGwAZQBfAHMAbwB1AHIAYwBlAC8AYwByAGUAZABlAG4
                                    AdABpAGEAbABzAC8ASQBuAHYAbwBrAGUALQBNAGkAbQBpAGsAYQB0AHoALgBwAHMAMQAiACkAOwAgAEkAbgB2AG8Aaw
                                    BlAC0ATQBpAG0AaQBrAGEAdAB6ACAALQBDAG8AbQBtAGEAbgBkACAAcAByAGkAdgBpAGwAZQBnAGUAOgA6AGQAZQBiAH
                                    UAZwA7ACAASQBuAHYAbwBrAGUALQBNAGkAbQBpAGsAYQB0AHoAIAAtAEQAdQBtAHAAQwByAGUAZABzADsA
                                """)

string_decoded = bytes_decoded.decode("utf-8")

print(" ")
print(string_decoded)
print(" ")