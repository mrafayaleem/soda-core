# Generated from /Users/vijay/work/soda/code/soda-core/soda/core/soda/sodacl/antlr/SodaCLAntlr.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,57,487,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,
        1,9,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,
        1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,26,
        1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,31,1,31,
        1,31,1,31,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,34,1,34,1,35,
        1,35,1,36,1,36,1,37,1,37,1,38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,
        1,42,1,42,1,43,1,43,1,44,1,44,1,44,1,45,1,45,1,45,1,46,1,46,1,46,
        1,47,1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,51,1,51,1,51,1,51,
        4,51,453,8,51,11,51,12,51,454,1,51,1,51,1,52,1,52,1,52,1,52,4,52,
        463,8,52,11,52,12,52,464,1,52,1,52,1,53,1,53,5,53,471,8,53,10,53,
        12,53,474,9,53,1,54,4,54,477,8,54,11,54,12,54,478,1,55,4,55,482,
        8,55,11,55,12,55,483,1,56,1,56,0,0,57,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,
        37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,
        59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,
        81,41,83,42,85,43,87,44,89,45,91,46,93,47,95,48,97,49,99,50,101,
        51,103,52,105,53,107,54,109,55,111,56,113,57,1,0,6,1,0,34,34,1,0,
        96,96,3,0,65,90,95,95,97,122,6,0,32,32,40,41,44,44,60,62,91,91,93,
        93,4,0,48,57,65,90,95,95,97,122,1,0,48,57,493,0,1,1,0,0,0,0,3,1,
        0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,
        0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,
        0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,
        0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,
        0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,
        0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,
        0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,
        0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,
        0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,
        0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,
        0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,
        113,1,0,0,0,1,115,1,0,0,0,3,131,1,0,0,0,5,136,1,0,0,0,7,154,1,0,
        0,0,9,162,1,0,0,0,11,181,1,0,0,0,13,201,1,0,0,0,15,209,1,0,0,0,17,
        228,1,0,0,0,19,230,1,0,0,0,21,232,1,0,0,0,23,234,1,0,0,0,25,244,
        1,0,0,0,27,258,1,0,0,0,29,269,1,0,0,0,31,276,1,0,0,0,33,295,1,0,
        0,0,35,312,1,0,0,0,37,327,1,0,0,0,39,343,1,0,0,0,41,346,1,0,0,0,
        43,348,1,0,0,0,45,352,1,0,0,0,47,356,1,0,0,0,49,364,1,0,0,0,51,368,
        1,0,0,0,53,371,1,0,0,0,55,376,1,0,0,0,57,381,1,0,0,0,59,386,1,0,
        0,0,61,393,1,0,0,0,63,398,1,0,0,0,65,402,1,0,0,0,67,406,1,0,0,0,
        69,410,1,0,0,0,71,412,1,0,0,0,73,414,1,0,0,0,75,416,1,0,0,0,77,418,
        1,0,0,0,79,420,1,0,0,0,81,422,1,0,0,0,83,424,1,0,0,0,85,426,1,0,
        0,0,87,428,1,0,0,0,89,430,1,0,0,0,91,433,1,0,0,0,93,436,1,0,0,0,
        95,439,1,0,0,0,97,442,1,0,0,0,99,444,1,0,0,0,101,446,1,0,0,0,103,
        448,1,0,0,0,105,458,1,0,0,0,107,468,1,0,0,0,109,476,1,0,0,0,111,
        481,1,0,0,0,113,485,1,0,0,0,115,116,5,102,0,0,116,117,5,114,0,0,
        117,118,5,101,0,0,118,119,5,115,0,0,119,120,5,104,0,0,120,121,5,
        110,0,0,121,122,5,101,0,0,122,123,5,115,0,0,123,124,5,115,0,0,124,
        125,5,32,0,0,125,126,5,117,0,0,126,127,5,115,0,0,127,128,5,105,0,
        0,128,129,5,110,0,0,129,130,5,103,0,0,130,2,1,0,0,0,131,132,5,119,
        0,0,132,133,5,105,0,0,133,134,5,116,0,0,134,135,5,104,0,0,135,4,
        1,0,0,0,136,137,5,114,0,0,137,138,5,111,0,0,138,139,5,119,0,0,139,
        140,5,95,0,0,140,141,5,99,0,0,141,142,5,111,0,0,142,143,5,117,0,
        0,143,144,5,110,0,0,144,145,5,116,0,0,145,146,5,32,0,0,146,147,5,
        115,0,0,147,148,5,97,0,0,148,149,5,109,0,0,149,150,5,101,0,0,150,
        151,5,32,0,0,151,152,5,97,0,0,152,153,5,115,0,0,153,6,1,0,0,0,154,
        155,5,100,0,0,155,156,5,101,0,0,156,157,5,102,0,0,157,158,5,97,0,
        0,158,159,5,117,0,0,159,160,5,108,0,0,160,161,5,116,0,0,161,8,1,
        0,0,0,162,163,5,115,0,0,163,164,5,97,0,0,164,165,5,109,0,0,165,166,
        5,101,0,0,166,167,5,32,0,0,167,168,5,100,0,0,168,169,5,97,0,0,169,
        170,5,121,0,0,170,171,5,32,0,0,171,172,5,108,0,0,172,173,5,97,0,
        0,173,174,5,115,0,0,174,175,5,116,0,0,175,176,5,32,0,0,176,177,5,
        119,0,0,177,178,5,101,0,0,178,179,5,101,0,0,179,180,5,107,0,0,180,
        10,1,0,0,0,181,182,5,115,0,0,182,183,5,97,0,0,183,184,5,109,0,0,
        184,185,5,101,0,0,185,186,5,32,0,0,186,187,5,100,0,0,187,188,5,97,
        0,0,188,189,5,121,0,0,189,190,5,32,0,0,190,191,5,108,0,0,191,192,
        5,97,0,0,192,193,5,115,0,0,193,194,5,116,0,0,194,195,5,32,0,0,195,
        196,5,109,0,0,196,197,5,111,0,0,197,198,5,110,0,0,198,199,5,116,
        0,0,199,200,5,104,0,0,200,12,1,0,0,0,201,202,5,112,0,0,202,203,5,
        101,0,0,203,204,5,114,0,0,204,205,5,99,0,0,205,206,5,101,0,0,206,
        207,5,110,0,0,207,208,5,116,0,0,208,14,1,0,0,0,209,210,5,97,0,0,
        210,211,5,110,0,0,211,212,5,111,0,0,212,213,5,109,0,0,213,214,5,
        97,0,0,214,215,5,108,0,0,215,216,5,121,0,0,216,217,5,32,0,0,217,
        218,5,115,0,0,218,219,5,99,0,0,219,220,5,111,0,0,220,221,5,114,0,
        0,221,222,5,101,0,0,222,223,5,32,0,0,223,224,5,102,0,0,224,225,5,
        111,0,0,225,226,5,114,0,0,226,227,5,32,0,0,227,16,1,0,0,0,228,229,
        5,100,0,0,229,18,1,0,0,0,230,231,5,104,0,0,231,20,1,0,0,0,232,233,
        5,109,0,0,233,22,1,0,0,0,234,235,5,118,0,0,235,236,5,97,0,0,236,
        237,5,108,0,0,237,238,5,117,0,0,238,239,5,101,0,0,239,240,5,115,
        0,0,240,241,5,32,0,0,241,242,5,105,0,0,242,243,5,110,0,0,243,24,
        1,0,0,0,244,245,5,109,0,0,245,246,5,117,0,0,246,247,5,115,0,0,247,
        248,5,116,0,0,248,249,5,32,0,0,249,250,5,101,0,0,250,251,5,120,0,
        0,251,252,5,105,0,0,252,253,5,115,0,0,253,254,5,116,0,0,254,255,
        5,32,0,0,255,256,5,105,0,0,256,257,5,110,0,0,257,26,1,0,0,0,258,
        259,5,99,0,0,259,260,5,104,0,0,260,261,5,101,0,0,261,262,5,99,0,
        0,262,263,5,107,0,0,263,264,5,115,0,0,264,265,5,32,0,0,265,266,5,
        102,0,0,266,267,5,111,0,0,267,268,5,114,0,0,268,28,1,0,0,0,269,270,
        5,102,0,0,270,271,5,105,0,0,271,272,5,108,0,0,272,273,5,116,0,0,
        273,274,5,101,0,0,274,275,5,114,0,0,275,30,1,0,0,0,276,277,5,99,
        0,0,277,278,5,111,0,0,278,279,5,110,0,0,279,280,5,102,0,0,280,281,
        5,105,0,0,281,282,5,103,0,0,282,283,5,117,0,0,283,284,5,114,0,0,
        284,285,5,97,0,0,285,286,5,116,0,0,286,287,5,105,0,0,287,288,5,111,
        0,0,288,289,5,110,0,0,289,290,5,115,0,0,290,291,5,32,0,0,291,292,
        5,102,0,0,292,293,5,111,0,0,293,294,5,114,0,0,294,32,1,0,0,0,295,
        296,5,102,0,0,296,297,5,111,0,0,297,298,5,114,0,0,298,299,5,32,0,
        0,299,300,5,101,0,0,300,301,5,97,0,0,301,302,5,99,0,0,302,303,5,
        104,0,0,303,304,5,32,0,0,304,305,5,100,0,0,305,306,5,97,0,0,306,
        307,5,116,0,0,307,308,5,97,0,0,308,309,5,115,0,0,309,310,5,101,0,
        0,310,311,5,116,0,0,311,34,1,0,0,0,312,313,5,102,0,0,313,314,5,111,
        0,0,314,315,5,114,0,0,315,316,5,32,0,0,316,317,5,101,0,0,317,318,
        5,97,0,0,318,319,5,99,0,0,319,320,5,104,0,0,320,321,5,32,0,0,321,
        322,5,116,0,0,322,323,5,97,0,0,323,324,5,98,0,0,324,325,5,108,0,
        0,325,326,5,101,0,0,326,36,1,0,0,0,327,328,5,102,0,0,328,329,5,111,
        0,0,329,330,5,114,0,0,330,331,5,32,0,0,331,332,5,101,0,0,332,333,
        5,97,0,0,333,334,5,99,0,0,334,335,5,104,0,0,335,336,5,32,0,0,336,
        337,5,99,0,0,337,338,5,111,0,0,338,339,5,108,0,0,339,340,5,117,0,
        0,340,341,5,109,0,0,341,342,5,110,0,0,342,38,1,0,0,0,343,344,5,36,
        0,0,344,345,5,123,0,0,345,40,1,0,0,0,346,347,5,46,0,0,347,42,1,0,
        0,0,348,349,5,102,0,0,349,350,5,111,0,0,350,351,5,114,0,0,351,44,
        1,0,0,0,352,353,5,97,0,0,353,354,5,110,0,0,354,355,5,100,0,0,355,
        46,1,0,0,0,356,357,5,98,0,0,357,358,5,101,0,0,358,359,5,116,0,0,
        359,360,5,119,0,0,360,361,5,101,0,0,361,362,5,101,0,0,362,363,5,
        110,0,0,363,48,1,0,0,0,364,365,5,110,0,0,365,366,5,111,0,0,366,367,
        5,116,0,0,367,50,1,0,0,0,368,369,5,105,0,0,369,370,5,110,0,0,370,
        52,1,0,0,0,371,372,5,119,0,0,372,373,5,97,0,0,373,374,5,114,0,0,
        374,375,5,110,0,0,375,54,1,0,0,0,376,377,5,102,0,0,377,378,5,97,
        0,0,378,379,5,105,0,0,379,380,5,108,0,0,380,56,1,0,0,0,381,382,5,
        112,0,0,382,383,5,97,0,0,383,384,5,115,0,0,384,385,5,115,0,0,385,
        58,1,0,0,0,386,387,5,99,0,0,387,388,5,104,0,0,388,389,5,97,0,0,389,
        390,5,110,0,0,390,391,5,103,0,0,391,392,5,101,0,0,392,60,1,0,0,0,
        393,394,5,108,0,0,394,395,5,97,0,0,395,396,5,115,0,0,396,397,5,116,
        0,0,397,62,1,0,0,0,398,399,5,97,0,0,399,400,5,118,0,0,400,401,5,
        103,0,0,401,64,1,0,0,0,402,403,5,109,0,0,403,404,5,105,0,0,404,405,
        5,110,0,0,405,66,1,0,0,0,406,407,5,109,0,0,407,408,5,97,0,0,408,
        409,5,120,0,0,409,68,1,0,0,0,410,411,5,91,0,0,411,70,1,0,0,0,412,
        413,5,93,0,0,413,72,1,0,0,0,414,415,5,123,0,0,415,74,1,0,0,0,416,
        417,5,125,0,0,417,76,1,0,0,0,418,419,5,40,0,0,419,78,1,0,0,0,420,
        421,5,41,0,0,421,80,1,0,0,0,422,423,5,44,0,0,423,82,1,0,0,0,424,
        425,5,37,0,0,425,84,1,0,0,0,426,427,5,43,0,0,427,86,1,0,0,0,428,
        429,5,45,0,0,429,88,1,0,0,0,430,431,5,33,0,0,431,432,5,61,0,0,432,
        90,1,0,0,0,433,434,5,60,0,0,434,435,5,62,0,0,435,92,1,0,0,0,436,
        437,5,60,0,0,437,438,5,61,0,0,438,94,1,0,0,0,439,440,5,62,0,0,440,
        441,5,61,0,0,441,96,1,0,0,0,442,443,5,61,0,0,443,98,1,0,0,0,444,
        445,5,60,0,0,445,100,1,0,0,0,446,447,5,62,0,0,447,102,1,0,0,0,448,
        452,5,34,0,0,449,453,8,0,0,0,450,451,5,92,0,0,451,453,5,34,0,0,452,
        449,1,0,0,0,452,450,1,0,0,0,453,454,1,0,0,0,454,452,1,0,0,0,454,
        455,1,0,0,0,455,456,1,0,0,0,456,457,5,34,0,0,457,104,1,0,0,0,458,
        462,5,96,0,0,459,463,8,1,0,0,460,461,5,92,0,0,461,463,5,96,0,0,462,
        459,1,0,0,0,462,460,1,0,0,0,463,464,1,0,0,0,464,462,1,0,0,0,464,
        465,1,0,0,0,465,466,1,0,0,0,466,467,5,96,0,0,467,106,1,0,0,0,468,
        472,7,2,0,0,469,471,8,3,0,0,470,469,1,0,0,0,471,474,1,0,0,0,472,
        470,1,0,0,0,472,473,1,0,0,0,473,108,1,0,0,0,474,472,1,0,0,0,475,
        477,7,4,0,0,476,475,1,0,0,0,477,478,1,0,0,0,478,476,1,0,0,0,478,
        479,1,0,0,0,479,110,1,0,0,0,480,482,7,5,0,0,481,480,1,0,0,0,482,
        483,1,0,0,0,483,481,1,0,0,0,483,484,1,0,0,0,484,112,1,0,0,0,485,
        486,5,32,0,0,486,114,1,0,0,0,8,0,452,454,462,464,472,478,483,0
    ]

class SodaCLAntlrLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    FOR = 22
    AND = 23
    BETWEEN = 24
    NOT = 25
    IN = 26
    WARN = 27
    FAIL = 28
    PASS = 29
    CHANGE = 30
    LAST = 31
    AVG = 32
    MIN = 33
    MAX = 34
    SQUARE_LEFT = 35
    SQUARE_RIGHT = 36
    CURLY_LEFT = 37
    CURLY_RIGHT = 38
    ROUND_LEFT = 39
    ROUND_RIGHT = 40
    COMMA = 41
    PERCENT = 42
    PLUS = 43
    MINUS = 44
    NOT_EQUAL = 45
    NOT_EQUAL_SQL = 46
    LTE = 47
    GTE = 48
    EQUAL = 49
    LT = 50
    GT = 51
    IDENTIFIER_DOUBLE_QUOTE = 52
    IDENTIFIER_BACKTICK = 53
    IDENTIFIER_UNQUOTED = 54
    NAME = 55
    DIGITS = 56
    S = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'freshness using'", "'with'", "'row_count same as'", "'default'", 
            "'same day last week'", "'same day last month'", "'percent'", 
            "'anomaly score for '", "'d'", "'h'", "'m'", "'values in'", 
            "'must exist in'", "'checks for'", "'filter'", "'configurations for'", 
            "'for each dataset'", "'for each table'", "'for each column'", 
            "'${'", "'.'", "'for'", "'and'", "'between'", "'not'", "'in'", 
            "'warn'", "'fail'", "'pass'", "'change'", "'last'", "'avg'", 
            "'min'", "'max'", "'['", "']'", "'{'", "'}'", "'('", "')'", 
            "','", "'%'", "'+'", "'-'", "'!='", "'<>'", "'<='", "'>='", 
            "'='", "'<'", "'>'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "FOR", "AND", "BETWEEN", "NOT", "IN", "WARN", "FAIL", "PASS", 
            "CHANGE", "LAST", "AVG", "MIN", "MAX", "SQUARE_LEFT", "SQUARE_RIGHT", 
            "CURLY_LEFT", "CURLY_RIGHT", "ROUND_LEFT", "ROUND_RIGHT", "COMMA", 
            "PERCENT", "PLUS", "MINUS", "NOT_EQUAL", "NOT_EQUAL_SQL", "LTE", 
            "GTE", "EQUAL", "LT", "GT", "IDENTIFIER_DOUBLE_QUOTE", "IDENTIFIER_BACKTICK", 
            "IDENTIFIER_UNQUOTED", "NAME", "DIGITS", "S" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "FOR", "AND", "BETWEEN", "NOT", "IN", "WARN", 
                  "FAIL", "PASS", "CHANGE", "LAST", "AVG", "MIN", "MAX", 
                  "SQUARE_LEFT", "SQUARE_RIGHT", "CURLY_LEFT", "CURLY_RIGHT", 
                  "ROUND_LEFT", "ROUND_RIGHT", "COMMA", "PERCENT", "PLUS", 
                  "MINUS", "NOT_EQUAL", "NOT_EQUAL_SQL", "LTE", "GTE", "EQUAL", 
                  "LT", "GT", "IDENTIFIER_DOUBLE_QUOTE", "IDENTIFIER_BACKTICK", 
                  "IDENTIFIER_UNQUOTED", "NAME", "DIGITS", "S" ]

    grammarFileName = "SodaCLAntlr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


