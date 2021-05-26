# # purpose - to promt user list of integers and promt over if greater than 100
# ListofInt = []
# print(" This list can add up to 10 elements")
# print("\n")
# for i in range(1, 10):
#     a = int(input("Enter the number "))
#     if a < 100:
#         ListofInt.append(a)
#     else:
#         ListofInt.append("over")
# print(ListofInt)
list1= ["Ganool", "@Rarefilms", "@CC_ALL", "dvdrip", "@", "ALL", "@Rᴀʀᴇꜰɪʟᴍs", "BRRip", "x264", "ESubs", "esubs",
          "DVDRip", "RiYi", "EGY", "VHSRip", "HC", "YT", "AVC", "WEBRip", "Webrip", "webrip", "WEB-DL", "BRRip", "JAP",
          "XviD", "NF", "DL", "CHS", "WAR", "SL", "TMS", "RARBG", "YIFY", "MP3", "mp3", "AC3", "BDRip", "BLRV", "HDTV",
          "LeLe", "VHSRip", "R2", "WEB", "DOCU", "LiMiTED", "pLUS", "TVRip", "SH", "PL", "SPA", "Mkvking", "VXT", "EST",
          "ViET", "RiFi", "Ganool", "GalaxyRG", "ozlem", "H264", "AMZN", "DDP", "HEB", "AVC", "DVD", "DD2", "PRiME",
          "CC"]  # Work Around
list2= ["CC", "@Rarefilms", "@CC_ALL", "dvdrip", "@", "ALL", "@Rᴀʀᴇꜰɪʟᴍs", "BRRip", "x264", "ESubs", "esubs",
          "DVDRip", "RiYi", "EGY", "VHSRip", "HC", "YT", "AVC", "WEBRip", "Webrip", "webrip", "WEB-DL", "BRRip", "JAP",
          "XviD", "NF", "DL", "CHS", "WAR", "SL", "TMS", "RARBG", "YIFY", "MP3", "mp3", "AC3", "BDRip", "BLRV", "HDTV",
          "LeLe", "VHSRip", "R2", "WEB", "DOCU", "LiMiTED", "pLUS", "TVRip", "SH", "PL", "SPA", "Mkvking", "VXT", "EST",
          "ViET", "RiFi", "Ganool", "GalaxyRG", "ozlem", "H264", "AMZN", "DDP", "HEB", "AVC", "DVD", "DD2", "PRiME"]

print(len(list1))
print(len(list2))
list3 =[x for x in list1 if x in list2]
print((list3))
set1=set(list1)
set2 = set(list2)
print(set1.intersection(set2))