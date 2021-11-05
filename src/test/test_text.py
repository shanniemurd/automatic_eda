import os, sys, unittest
import pandas as pd
import numpy as np

# Class defining the unit tests for functions in TextColumn class

if os.path.abspath('.') not in sys.path:
    sys.path.append(os.path.abspath('.'))

from src.text import TextColumn

test_df = pd.DataFrame({'Date': ["19/06/2019", "13/06/2019", "07/06/2019", "28/05/2019", "22/05/2019", "10/05/2019", "13/04/2019", "11/04/2019", "11/04/2019", "09/04/2019", "06/04/2019", "30/03/2019", "18/03/2019", "16/03/2019", "15/03/2019", "09/03/2019", "21/02/2019", "20/02/2019", "05/02/2019", "25/01/2019", "21/12/2018", "19/12/2018", "19/12/2018", "15/12/2018", "15/12/2018", "11/12/2018", "05/12/2018", "30/11/2018", "28/11/2018", "20/11/2018", "17/11/2018", "16/11/2018", "03/11/2018", "30/10/2018", "20/10/2018", "19/10/2018", "10/10/2018", "06/10/2018", "28/09/2018", "26/09/2018", "24/09/2018", "22/09/2018", "22/09/2018", "17/09/2018", "13/09/2018", "09/09/2018", "08/09/2018", "07/09/2018", "05/09/2018", "01/09/2018", "29/08/2018", "24/08/2018", "22/08/2018", "21/08/2018", "17/08/2018", "27/06/2018", "23/06/2018", "21/06/2018", "16/06/2018", "08/06/2018", "07/06/2018", "26/05/2018", "26/05/2018", "26/05/2018", "26/05/2018", "22/05/2018", "16/05/2018", "12/05/2018", "12/05/2018", "06/05/2018", "05/05/2018", "28/04/2018", "27/04/2018", "20/04/2018", "17/04/2018", "14/04/2018", "12/04/2018", "10/04/2018", "09/04/2018", "08/04/2018", "06/04/2018", "06/04/2018", "29/03/2018", "24/03/2018", "22/03/2018", "22/03/2018", "17/03/2018", "17/03/2018", "17/03/2018", "16/03/2018", "13/03/2018", "10/03/2018", "08/03/2018", "07/03/2018", "07/03/2018", "02/03/2018", "26/02/2018", "24/02/2018", "24/02/2018", "21/02/2018", "21/02/2018", "17/02/2018", "07/02/2018", "07/02/2018", "30/01/2018", "05/01/2018", "15/12/2017", "11/12/2017", "10/12/2017", "09/12/2017", "08/12/2017", "07/12/2017", "07/12/2017", "06/12/2017", "06/12/2017", "02/12/2017", "01/12/2017", "24/11/2017", "22/11/2017", "22/11/2017", "21/11/2017", "17/11/2017", "10/11/2017", "10/11/2017", "09/11/2017", "04/11/2017", "03/11/2017", "03/11/2017", "02/11/2017", "27/10/2017", "26/10/2017", "23/10/2017", "19/10/2017", "17/10/2017", "14/10/2017", "13/10/2017", "13/10/2017", "11/10/2017", "10/10/2017", "06/10/2017", "04/10/2017", "30/09/2017", "26/09/2017", "15/09/2017", "14/09/2017", "13/09/2017", "13/09/2017", "13/09/2017", "13/09/2017", "12/09/2017", "02/09/2017", "01/09/2017", "23/08/2017", "23/08/2017", "22/08/2017", "21/08/2017", "21/08/2017", "19/08/2017", "16/08/2017", "16/08/2017", "11/08/2017", "10/08/2017", "05/08/2017", "04/08/2017", "02/08/2017", "01/08/2017", "29/07/2017", "29/07/2017", "26/07/2017", "21/07/2017", "05/07/2017", "01/07/2017", "30/06/2017", "24/06/2017", "24/06/2017", "24/06/2017", "23/06/2017", "21/06/2017", "21/06/2017", "20/06/2017", "17/06/2017", "16/06/2017", "15/06/2017", "03/06/2017", "03/06/2017", "02/06/2017", "27/05/2017", "26/05/2017", "24/05/2017", "24/05/2017", "17/05/2017", "17/05/2017", "13/05/2017", "11/05/2017", "06/05/2017", "03/05/2017", "03/05/2017", "26/04/2017", "21/04/2017", "18/04/2017", "13/04/2017", "11/04/2017", "08/04/2017", "08/04/2017", "08/04/2017", "07/04/2017", "07/04/2017", "04/04/2017", "01/04/2017", "31/03/2017", "29/03/2017", "29/03/2017", "29/03/2017", "27/03/2017", "25/03/2017", "21/03/2017", "20/03/2017", "18/03/2017", "18/03/2017", "15/03/2017", "15/03/2017", "14/03/2017", "11/03/2017", "11/03/2017", "11/03/2017", "11/03/2017", "04/03/2017", "04/03/2017", "03/03/2017", "01/03/2017", "01/03/2017", "01/03/2017", "28/02/2017", "13/02/2017", "10/02/2017", "08/02/2017", "08/02/2017", "02/02/2017", "28/01/2017", "25/01/2017", "23/01/2017", "31/12/2016", "17/12/2016", "17/12/2016", "17/12/2016", "17/12/2016", "10/12/2016", "08/12/2016", "08/12/2016", "26/11/2016", "18/11/2016", "17/11/2016", "16/11/2016", "11/11/2016", "11/11/2016", "07/11/2016", "07/11/2016", "29/10/2016", "26/10/2016", "26/10/2016", "21/10/2016", "19/10/2016", "19/10/2016", "18/10/2016", "13/10/2016", "13/10/2016", "13/10/2016", "12/10/2016", "12/10/2016", "12/10/2016", "10/10/2016", "07/10/2016", "01/10/2016", "27/09/2016", "26/09/2016", "26/09/2016", "21/09/2016", "21/09/2016", "14/09/2016", "14/09/2016", "13/09/2016", "10/09/2016", "10/09/2016", "05/09/2016", "03/09/2016", "28/08/2016", "27/08/2016", "27/08/2016", "26/08/2016", "17/08/2016", "13/08/2016", "12/08/2016", "16/07/2016", "12/07/2016", "05/07/2016", "02/07/2016", "21/06/2016", "21/06/2016", "20/06/2016", "09/06/2016"],
                        'Id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300],
                        'suburb': ["Avalon Beach", np.nan, "", "Avalon Beach", "Whale Beach", "Bilgola Plateau", np.nan, "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Whale Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Whale Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Clareville", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Bilgola Plateau", "Clareville", "Bilgola Plateau", "Avalon Beach", "Whale Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Clareville", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Clareville", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Clareville", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Whale Beach", "Bilgola Plateau", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Whale Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Whale Beach", "Bilgola Plateau", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Clareville", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Whale Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Clareville", "Avalon Beach", "Avalon Beach", "Clareville", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Clareville", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Beach", "Bilgola Plateau", "Bilgola Beach", "Avalon Beach", "Whale Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", ""],
                        'postalCode': ["2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", ""],
                        'bed': [4, 4, 3, 3, 5, 4, 3, 5, 3, 3, 4, 6, 4, 4, 4, 5, 4, 3, 3, 4, 2, 4, 4, 3, 3, 3, 5, 4, 3, 3, 4, 5, 6, 4, 4, 4, 4, 4, 5, 5, 5, 4, 4, 4, 3, 4, 4, 4, 6, 3, 3, 4, 3, 5, 3, 3, 5, 4, 4, 5, 5, 6, 5, 3, 5, 6, 5, 3, 3, 4, 4, 4, 4, 4, 5, 3, 4, 5, 3, 3, 3, 4, 4, 4, 4, 3, 5, 3, 3, 4, 3, 4, 5, 3, 3, 4, 3, 4, 4, 4, 3, 4, 2, 4, 4, 3, 4, 4, 4, 5, 4, 4, 2, 4, 3, 5, 3, 3, 4, 3, 6, 3, 4, 3, 4, 4, 4, 2, 5, 3, 4, 4, 4, 5, 4, 5, 3, 3, 4, 5, 3, 3, 4, 6, 7, 3, 3, 3, 3, 3, 4, 4, 4, 2, 4, 5, 2, 6, 4, 4, 4, 4, 3, 3, 4, 4, 5, 6, 4, 3, 5, 5, 5, 5, 2, 4, 3, 4, 3, 4, 3, 3, 3, 3, 4, 3, 4, 3, 3, 3, 4, 4, 3, 4, 3, 4, 4, 4, 3, 4, 3, 3, 5, 4, 4, 5, 3, 4, 5, 4, 5, 2, 5, 4, 5, 3, 4, 4, 3, 4, 2, 2, 4, 4, 6, 3, 3, 4, 3, 4, 3, 4, 4, 4, 5, 4, 4, 4, 5, 5, 2, 5, 3, 2, 4, 3, 4, 5, 3, 5, 5, 3, 3, 4, 4, 5, 3, 4, 2, 4, 4, 5, 3, 3, 3, 4, 3, 3, 3, 3, 4, 4, 4, 3, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 2, 4, 4, 3, 4, 3, 4, 5, 3, 3, 4, 4, 5, 3, 3, 2],
                        'propType': ["HOUSE", " ", "1232", "53", " ", "", "house", "house", " ", "house", "", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "townhouse", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "townhouse", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "duplex/semi-detached", "house", "house", "house", "house", "townhouse", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "townhouse", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "townhouse", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "duplex/semi-detached", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "townhouse", "townhouse", "townhouse", "house", "house", "townhouse", "house", "house", "townhouse", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", ""]})


class TestTextColum_functions(unittest.TestCase):

    def test_get_unique(self):
        Text_stats = TextColumn('suburb', test_df)

        no_unique_values = Text_stats.get_unique()
        expected_no_unique_values = 7

        # check if the result generate by get_unique match expected result
        self.assertEqual(no_unique_values, expected_no_unique_values)

    def test_get_missing(self):
        Text_stats = TextColumn('suburb', test_df)

        no_missing_values = Text_stats.get_missing()
        expected_no_missing_values = 2

        # check if the result generate by get_missing match expected result
        self.assertEqual(no_missing_values, expected_no_missing_values)

    def test_get_empty(self):
        Text_stats = TextColumn('suburb', test_df)

        no_empty = Text_stats.get_empty()
        expected_no_empty = 4

        # check if the result generate by get_empty match expected result
        self.assertEqual(no_empty, expected_no_empty)

    def test_get_whitespace(self):
        Text_stats = TextColumn('propType', test_df)

        no_whitespace = Text_stats.get_whitespace()
        expected_no_whitespace = 3

        # check if the result generate by get_whitespace match expected result
        self.assertEqual(no_whitespace, expected_no_whitespace)

    def test_get_lowercase(self):
        Text_stats = TextColumn('propType', test_df)

        no_lowercase = Text_stats.get_lowercase()
        expected_no_lowercase = 291

        # check if the result generate by get_lowercase match expected result
        self.assertEqual(no_lowercase, expected_no_lowercase)

    def test_get_uppercase(self):
        Text_stats = TextColumn('propType', test_df)

        no_uppercase = Text_stats.get_uppercase()
        expected_no_uppercase = 1

        # check if the result generate by get_uppercase match expected result
        self.assertEqual(no_uppercase, expected_no_uppercase)

    def test_get_alphabet(self):
        Text_stats = TextColumn('propType', test_df)

        no_alphabet = Text_stats.get_alphabet()
        expected_no_alphabet = 290

        # check if the result generate by get_alphabet match expected result
        self.assertEqual(no_alphabet, expected_no_alphabet)

    def test_get_digit(self):
        Text_stats = TextColumn('propType', test_df)

        no_digit = Text_stats.get_digit()
        expected_no_digit = 2

        # check if the result generate by get_digit match expected result
        self.assertEqual(no_digit, expected_no_digit)

    def test_get_mode(self):
        Text_stats = TextColumn('propType', test_df)

        str_mode = Text_stats.get_mode()
        expected_str_mode = 'house'

        # check if the result generate by get_mode match expected result
        self.assertEqual(str_mode, expected_str_mode)


    def test_get_barchart(self):
        Text_stats = TextColumn('propType', test_df)

        chart_data = Text_stats.get_barchart()
        expected_chart_data_index = 'house'

        # check if the chart_data generate by get_barchart match expected result
        self.assertIn(expected_chart_data_index, chart_data.index)

    def test_get_frequent(self):
        Text_stats = TextColumn('propType', test_df)

        frequency_table = Text_stats.get_frequent()

        # check if the result generate by get_frequent match expected result
        self.assertEqual(279, frequency_table.occurrence[frequency_table.value == 'house'].values[0])
        self.assertEqual(0.93, round(frequency_table.percentage[frequency_table.value == 'house'].values[0], 2))

    def test_construct_table(self):
        Text_stats = TextColumn('propType', test_df)

        table = Text_stats.construct_table()

        # check if the shape of the table generate by construct_table match is as expected
        self.assertEqual(9, table.shape[0])
        self.assertEqual(1, table.shape[1])

        self.assertEqual(table.value[table.index == 'number of unique values'].values[0], '8')
        self.assertEqual(table.value[table.index == 'number of missing values'].values[0], '0')
        self.assertEqual(table.value[table.index == 'number of rows with empty string'].values[0], '3')
        self.assertEqual(table.value[table.index == 'number of rows with only whitespaces'].values[0], '3')
        self.assertEqual(table.value[table.index == 'number of rows with only lower case characters'].values[0], '291')
        self.assertEqual(table.value[table.index == 'number of rows with only upper case characters'].values[0], '1')
        self.assertEqual(table.value[table.index == 'number of rows with only alphabet characters'].values[0], '290')
        self.assertEqual(table.value[table.index == 'number of rows with only numbers as characters'].values[0], '2')
        self.assertEqual(table.value[table.index == 'the mode value'].values[0], 'house')
    #




# python -m unittest src/test/test_text.py

if __name__ == '__main__':
    unittest.main()

