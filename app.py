import streamlit as st
from streamlit_option_menu import option_menu
from app_home import run_home
from app_eda import run_eda
from app_ml import run_ml
from app_home_eng import run_home_eng
from app_eda_eng import run_eda_eng
from app_ml_eng import run_ml_eng

def main():
    st.set_page_config(
     page_title="생활패턴으로 비만지수 예측",
     page_icon="💉",
    #  layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://github.com/eyoo95/Streamlit_obesity',
         'Report a bug': 'https://startcod.tistory.com/',
     })
    
    with st.sidebar:
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQ4AAAC7CAMAAACjH4DlAAABgFBMVEUkN0b30LHvSU1MTEyXmJJ6al3zSU0ANkUKNEjfRku/Q0gfOUZFTEzuSU34SEn20LKOS01sS0v3R07vPEbzwKTyqJTyPkMmN0QmNkZ8PUhISEiTlZH70LBOTEr81rUXN0bLuKQANkbtyaxyY1gAJzw+QkUbMkQKL0JPSk3yR1DZRk/tSUlBTU5NOUf107IAKUEnNEkAOEI/TkzxSUWKi4VTU1DWtJzlxq3JvLbdwqw/REWRhXsbLz2Ff3qsmYpta2liPUiaQEmVhXdqOkjSRVKMPEg1TU2eP0mxS0/sSFRoTEykSkwyP0pIVFxkZWJjWlO9oImFb11zX12ehG+9rZ0AHjXXw7TGubOFem9ZXmHHqpKilo25Q008O0IbNjs1OUtQOEx1PkJYOkC1QE+uTEl6S0WYT0q/TEdLR1G6SEXMREZYOEsAMlDwcmhhSlGBNkR5PU/ymIiXcG2GS1FZTUYAOTuLTUbzq5fYm4twTUhKPD9ePkPCQFJdaW20pJgAEzIcFXi/AAAgAElEQVR4nOVdC1vbRrqWbTK2rBuoeyrhWhI2trAsY3ypcQmES8zFBocku2w2JAaapMk2ZLfJObB7TtucnL9+vpF8lUa27FISyts+T7hIRvPOd59vRhQ1DId3RmJel4d+xB8H+sPRbNx5/FD/3M95XehKwJ3Hd+YHYP2wjc/9lNcEjWmTcT8pJAHLXcA3glD9y7zNiPS5H/SaILWnX4jH44Ig5DsQhAD8JCA8tn99W2xH2haORypwEegDpgLjkS0dzc/9nNcCWavYdFTz8QARVVtbKrfClsqa7VjmVYHMRkCwpeN2uBZ5zabjsZr3oEN9fIvooKiQNdq/eNNx37ogdDvo0JttS+pBh6CuW9rSvB10UE0ca/256iEbgJX52+NZLDruzD9WvekQ7mDfclvogCD9L4+fefkVQPzR/b/M35YgndKP5yEc92YjEIBfz1d05nM/6DWheScZ8HIrtrYEknea8m2hQ59PCvkhygLqkpxfk29LDqf9eaiqYOlYfrhG3RY69MqjEXSojyqf+yGvEc3H8aG6IgQe3xo3C1h7GBA80lmbjvjh2ud+xutEc4TxSN4m4aCo1PJQNuJzqdtSC7OwcH9IjA50rC587ie8VujsUDrUtH5bvKyNYdoixFdSn/v5rhkLq97iIcTv3ZJSRw9Nz1JpIK7eLk0B6Kkjz0gsfnTbdAX4eOCZxOXZwud+umuH9Nc5lSwf6tFfb52ySHpMqJLFoyrclqJxD/LSkVpdUQUXI/GVavzT0ud+vOuFJC8dgmd58gQSOZzL4ZVqnMcK8fyTJ5DeH96qKEyi9GYVCBCefAcK01nEF+JqfuW7J2BK88lm5HM/43ViobmCzWhcePK3JytJ3NgQzweE6sp3f3uSjwM56op0a8yHRC1VqlYQBjxUn/ztb9999+S7J0++w6jGQVQsCxK6LbHHgv68V/uJCys2Ed+BZFRtLjAE4f7awi2olur6veRgwJEHJXny5MlKFQxp33KDWn268IfWGAkvV4eqmIwuHdYXtmMJDP40DoSEmrpO/UFlRNeldCUUG1EW7IOQjFXYNMQon/vJrx4wyU22ElJC6eFlwX6oy3dDilLJQZD6R9IafSFFHVcwF4D0M3ck6iUdz9IhC5UHx1RqQZf+CFqzkGquPkuqhzF7aHfXh5YFB6RjvU1H7KGanFtNp26+aV1Y21gOqIG4+jDUHtrq8BWnfjrud+g4xJ8gzG2s3exkZmFhtapa0iBUOnRseJfBnHR0JEp5aH+vVu+t3dwSu56CEEO1Y4lkh45QzLeyCOnOPZX2D+JAyF9v6Prc0rGdwFvheDLWGVq6Omw5sg/x5bTSoTDZpgNEZKWSuoFGVV9YF3pWAvvMDh2PfBkPIPJRRzqUAe8sPF+7eSb1QRW3mHdn+qhLR+ypP20RhKexLh3P1L6fqyuxG2dBBFzI6I5Bvd+lI6T4NB4906GAd+59lgBSt3E1+a5MFQqUxGhaJJEIAyKaJgOG3iNJEgPCH4nYd8AtuJzFjOjcGhyaeqc7Nr9xqfqsdwtIVH8/P+R6q0tXkcowDKMnws3NnR+i24DW3s7iqVakhhHCFHQ9oZ182KrDLefR+t6HEyahF0YlEo6xKT3hSPvSFkHd6FpfcC0O7xxXn1+FfMiRxOJe1hB5hCHyZV5sbO9IxaL36JjEaa1FG3AlAMH/fLARrZ2GR2zdGxxctW9o4FsCo5yLEIjPpXsUhmJVYaDVEAzIp98oH4xUiGizWaDCDAY5+J/jDIPjgojnP9YSmvuGAkMxcvjsFS0iFIQrLcB9mMlG66RYYIYw4hD8u310xO6MisRw+XQ+1EdH+pnziri6/ttCVF0L73B8GQbkAi/StYhrcMCf1qwjnnQHKqOPdyND7McgHffTfXSE0qPzFmF94I67q05tCeTV9d+gLxJVrGXLhkEYGgyOM/jooubkQy/uBMschwh3GCgoinu6t5L1P7qghgYRe6YO6Q2Lgyo8ujt4x0OnQIF/UVeXJozHsDPZA5E3iWzAj/GgZyN9g2MkRj/ZRpZWkW7h4BYx+33Yqze4/9Hz1fTg4FjMh7dkxNV1xw3KXfeSHVy28Y8JzYd2ts2TJaMnInyr2FMYuRDeNIia1UeJiGbBgoyiQ3CPLpR+mvRUGCG5cbffcOAbmo/cl4OFeTBZfKr9QiPkIRp9o4ue9j6+OCt6CEbfHZy4FSb/xYHHngfHwmYG9eUuTnbjvc2ScWvfKKSty0/vDmpKhs2woXk1T2hjX5mg2o7FvkEyAC7w28CH9flyYtbXHZx4APpCsCB9zxy3dCVT+kmBYfUZ1PTD+8+qgtoG/iK58uj+ZdohSpY0KekkoQEirn5Kjb1+KRVOGmXRz+AMfttyuOBfXxhEj+KCyc8WSfaj/6EtXcmwF4N0KKFYLJ2OVeafPr1///7q0zsPQ/B9OqQoLjpCM0r6EcHaYPMxdvoia1mERo8NjCMyUCuMp1p7aZicLzoQJ76IECao/6kf4iCMzb1lWfdAQW26IP3WxgEbc/mWtuR5CkeT5PXgZ+FXPsjAaIEIofcJfJs/5bIJMc4IBq3vkecs6VeURk4h8jEa+61SKD1Hcs1C/JNH9KHNnpDoYLTaKJ/SHlZjlod/uCYQWC/7usWCUY4mhtGh3rGmnd0XS5OREWKns0CHR6qjHpO9S/jVIunHDEV7hRsOOs4/8Nh8RBPaJmiNbzqChvhec4lsb/pWbD/xYJonGAU/UHI/0DlWSa8QI7f8HFk8wlkSHUxkx+fIxL0awhYEbUayY5CBicyeuhK6Lh3qvG0T2Lf85WR0ZErZBqbjjod4kK2pjH4l5GGU5NcMoNoidj8QfWzyY7EBTO64rGnX1h21/WYuy89MaDrYIIfvTC8Ty4rx6l8Jw9Y2+RqBjn+8QT7NADo74bGnCBr0mGwEg7TrL3eloy0coctG+WJCOmYQp4Qyodi8QNpQKKhPCeKhbYEKE36cHRVadpBNMONKRQec6JqJzsN2asbsa8RfhCayHj++EY1LxRIPoroQW9jDUX7LTQdYRV8BGIhFKxyZlA5U/uiM1dt2tO1WQFcOeOONO970g1IUBS09Y8nOJa/ecekqkwgiFx0yE6n7tRwgW8XGhHRw5YbkKDC26VjpxFZsFKGD3GR0QBQ5Y30VI27cz6tu58IsIrHu9v/FrM8B8dxLLTymR+nC4MRfHZui21a/W/dhacTXSxMpyyV4/wsrok0TdwXl86ors2VmecMdDjEnPu2oYTYYZlwH24UJXjpySqAj0GYjE9o3g8bfJ5OO1yiIpn+0zPDdALEdIu4sFDKRFhLPww7vLzM1n+bAROcRuQgCPRkfEMM5OkHtx/zUEY7cNELG+SR0KOwPQMcb2yndJSVyuELitB0g6Ah8g+On2pZf0xHci8jh1sR0BGmHNbN1ZaPtWpVSXUQcPUmUzubOgY622YmRQzFB3XBoy6lowiM5Kw+RqM/xcRC0yInWxGwERcf8WDpdvcu2rQWYQwheJ0paSmDg0du2YKVJbASEgGMLjFYDf0o7S0NS5NwvHeUzmdL2eMNnkOICWhycH+spu+sJbAY+F9EThWH7OM/+e/tW1wpDmw9hcONtYg/nG2eOwqXk3zhmwe5oO6LfmM1NhyMQs0T4fsfN5l4gnDJPQgf7BsfKHbNzl7zjVHAkLpHtMjzToqMuJSVov7ajFcYlAp8hGwH8Bzcd8cMuHQf4OYxJhIN9i5nM7trfxTbICxLq0YBv0RomFthBXaHksN/0A4IwkI6av4Ig8QNmB12LpdHdMZUsGyZOUv4p4RlFdK5thBSPBYlkv/HQFvFAxJrTlPqmw/gFwijtnedKzEigFy7pyCfTPyp9YwqK+37pUDKlTl1VwaUXxLWtsJL2aNNVj/VuXMxoOzxeF3M8EiWPCEqR0Rk9LRUYWV8csbAyBM50Gj/iyk5OsZcTLoPYtPEzfkVCyUy32WBf2wrccUppjwO21NUFrWbbU0YutnA5FO3oTjqiw6JSket4VrRdLJwy1NnkdBA8S36Zxnk5HtOFVUnhfWf4ygw4ZUuycgciwus5nVY7LzriR6lE1J4SqaBl8T38nmOZVY4MjSTQ9js7aG3wWxFKlhitJy7jwig6UzhB+NPXF/YYcpBI0jQnTvsMSxUwvRlMJBsqnZf5bZNDbT3LeNEhJFNFrm7ZL0k/MUwUNcVWYvCZpMjOsCAd1ROIw2JllGs6U9OlRGNSNoK0I8PH0vGfX7dsGYfAErXOx0hpc1F+Gud7GbYEIzvggqhTSfOyHYKa+16krTmRtRfIpOvwJ505nFYbJh187R/RMk7qOVHStT0N++UJtQVFCXT8k+ds/7iLgvz0uWjWOwZhFB2lBoradPzEB/kZLshf2MQqdz0Pbtx4zxuL2JfI4T3e/LiF0EfNjjs6Vk1mzoZNNydpH3jsS8xshEpkNSZybkel48fqaK/ozllgFPak7oOZ3982xXaovT+yaDpTDiLW0hoIwhqKaYj/tm5hLyp4XZckHfHnUbG8ZTUhRM6D/A5k+FlLd2R9Nmw/W8Gab4/BccEsJOXI6ueJRpgmV2ASUcwe6J3f6K1Dhilu6k7bkf/vr4J8HRPAToNli0WRaGf47PT5iOQFTAcS/13Cqd9bJGZ3aQMdsLYS1dfJOx6E+JGBPQL+22cNSMFmeUTjlFaizozOSrwUrose4s+Z4l6ECW9jAtB7Tdssy4xtec3g7NYYy074/mDDmUsHhPx/fhU06RyeYggs6d23YjvUzrX418PFoxTlkJ21QcCCftilUdk2Ozma/zFJ7pTJ/+lrhDjs35hNEaHmB/jOogOCy1dtTWYgtTPJfHA82tQpfQf7VvGEAaN7RkXq2CEi8UTmxrKppmFPywAdwj/LXNm4ZO3qXmu3jgyc0oJ1pPlzlh1WGCtx8PcbWIQyJipP72ZN9APmlc2I4p7HyR+YfQg1QD+0HWQ2wjUeBSnbkgA5nRhNoj0Cbw4yPvj9L1Yy8S853OJf6toWvtigtcjWWNkLx886y7T5eBKGhESY1YwCYry1CwqAU1rlRwWZ6N85bzoypRneMA3L7ryGid7fPUdmtK11kHonSdqSF/6Jo9ftMC6iw+XFTRRE1iptOGuAeLTpKL7yokO0nEERFyKiCUbL8ptWSgtoRfTTsawHajRdyqL+F5ZLLpvLQGBpoBlMB4eHlJmGb+lhLpc9KBvwXz2nsAc8MljIeEzL3ORA4bjWBmHrPhgPrP8IwRQnGmDZE4s4NIRJYs5AlyFItK2pvln2GALaSsiyHNmCi/ci2onB1yClxZaVn43IIHBeJpgA82PCuSiZP8KFODChl5Zh5JQS2NMg9p0lXNwfGpHt2lWabE4pRU2ULUFSy+GUVsGFsSD3/VzcbT6EP31lIp6DxFpaBMNTi5whhN4xVqwBI2wlbDq8Sx7ipgbhPfPSgPiD0TZF+CTGSml5rERaY4zslrD+pzbPcZ8dgnGXtmFMOfYCdCRjrbjCLwxuiDFlDasNS7xkYzR2TrkfxKBVWLy0njv6gFAwxaYDhJH/WIQ5BSFhZM5+LA1XgoL8YvsJw15dTTRwUWCoIngxmYpsmfz7IvMOpAPRYSA1MevfmKKss2ZNUesLkDT8nQuC0kNMhd3Ezzwn7sNYFcu4o4NSiPXADFwJzgjszj6YkDe50gEKGrtWOgcTb6J3z1XBifw/vzJokCXuNFHng1yCChsI4WXJ8Dak6QhCCY3BLejMacMktSfwEGsUZ/UCuGI6QSVaSNyKMIvICjAZWWaK2bIvbUEcNqQuOhZfgIWYjoLzV36C2XrDhvZ5Q8TW8QKhMkhe9uf9n2eI2D+AX8/Qhni+ewH37LPsG+CmhG0K5FQmx7cW/+QGbZqtWdEUa2ANYQhysWEiyMTwkj0nglGfXWzjgCZiJwG3MBSoCcT24SyPDiLMmZUXYxGjCjXybW5ktwm9YTyucP4Ew0H/vuCDwMOPlwjhlJaFyTPr8IgId7iTgEAG6NxbSFYUuFYsZULTEOcBkblt3sxui8Gy8fVXLogQPZ3BzLciphUjh2kQrwgeHgRYIngOvo1G2Np64URR1hf52dMChcd/hs1NhGE4bIUZ+V1N06gi6S7C5yT+RTi6CKyD2WAzZQ7VD0TTUFhFsYUEzKGZjXFcp8mdiPLb3AXkOReQ9oENZS9EzrgEU8ohswWahAyILdEgQAHFxXA2KGbfIWw0IMBERitRgKiDQ3LU6NTEOYPfKzJuUAyjzfKtiJyIvgT/AzMSDUvYR3FhsCTbYA0IN5E+RyLu/+BFg2+VclkwRVkDZbHhhBFAqK3A47V2t3jED4EIcQnWZxqybpCOGaBjhmVfg85M7360LzG+doIuhrdEE+EONwg4ElHQmSKMDiLiyEnfZ5v8YoSIxEe+ATKyKcm4RQhupiI0RDBgSaJijXwLAaQeG4qanZ6engnltsQGhL2QnoLmcxCUsewF2Mlplp0eiotL9se/g9EEz/SGZTP7oCyvWdwEIFYyl9PTs7Mfpv/7P5z4nzC1iG0tZzQgRoaEw9wOSxoui0dOZ3t4P/shSkbDBB+Lu2TxghM6BzrORRFUJ9zgaI9b3NgitqoljlmwEzAQvLAHSqIoLJ5qPKagCP7Wy6u0AYH6NF5QCBo//6iw+xDWTsdy5yLC/pY91gDVQH4QanIBTye+CS9Wh8E50EUNB6ezYEL6EYYPIgECKDu7CeOPocOU9tHkv9f0lyZHvJ4EcZHYlN60w202i6sFIi6SWplLbBcvnvqpESoVHCGLRonNsJcgYG9ylxyEpCVcJGtSetodeqjHerhu1WT3sDOoI9Qo4rRDdC4wgAP1cJooiwtIEMhiKxPGy5Kcxuh+u+tw8blOPrXI2quUqeR+wB+FrOQU7OJ5KdNWnVFgcQjKBY3znJJhFQ6v0r422uVFJa3rFUJL9qdUYRE3P1pLYNoWMo1iYrts0K7GhvBW2aOmw7/Dt1oL/SgsR+o85C94ZddfSAoe0WPLU2dUM+WgCeE2TjjAttG7r0Uwh0PT2S4hEH4gSFxwCRnrGSQ9HH+JlyqUB/rasTuvjVd16hQv6HJYHMBPIKSHYcKchTr8S8iRibNrtQzhxAUSIJmJbPFgOop+V2cg2qu5IzALnco3S8PMttp0BOnduilC8J0ZxkMHl9gu4gWGDEtDXLt7bpiN3QymoyLpBDoE9dhadUdZxqIDBctnL0VOdGXbkMktepSBzGzYssJY5c5w1WOT0Rf91n4Mvp7w2N/TGVOu1enOsMrpuW0rzfdFBy79WCXjTA4HmiXDKLfsuoDSJNIRf74QeWG7SLtMzH+/JaLgL66wqMBo7z1asSELloq4gs7xixCJGBCOvPdZ7OCMLOO126kr8hCTop+tRjfIPOgMDeGIz3p6Dicf1vBZbHb2DZNvd72AthyS6JhLSacQzG7hFEp7xyPxXdQUaWITfzFKXmNAOxH8GVhv3ulMDbKx8Ct/yQrYLLJX6acD0lPDsMu+OBG7KBto2o9jCVld7GjbsrrY7GRxcLsfatOxRqIjUF3Ti1EkblrKsgim5gWEEi1XE5AFmVzRQedhzWozRji03QQf5XfZ3zB2yH9pgA4YCm0tL7DTEFu+Bc/suxe71CjbCzVY42hsiTsu6ZhkSiGvTWvYguICBXhLoONADPLujmgL2qZhEvXlLLFjKRIkpvrLGkOd8T43Or11bzZ10xGb5u3lFUyHSI/T5VFq8ViSFEj7wNWBJYl2b20+IFUIIfKQJJHWcJsLpKOcmAVX/dJjv1xkmljREWcTLbsZfbZYaJ5hD+VvnxPtLBcT6YAk5Y29nvAap1Gir6jDvjF0wdvagdtD4L9Ow1xIUdJNIh0bOlXMRu3tm1gbcHCpeUgwGAWS+UDRBI3Hj8rgY2G2E694X5Uf42TYGby9UeWy9goarupYnt13/yCbabS/OLAeCfUtV6VIa7Xq6oIc2dqztpMwWgMFTcP86KXQjM5si+5VWMSdWk6YQ3sRChKYRNaPnzWNGlknXXSwb9pB16Utdb73LWSAhvbmj2mrgtboi1dSpM1P6voCpb2s2U+AEw/T4HfCHpsppYJ21nAXkjlkd1tC3o3jbV0SffTLgX8gbHEi0tENMhTrgxvjtA+220PYabyTol/NKvo6gY74p4XTQnv0Mu6hRpCwuLcedfiQNFKE1d7hYaX2QMcs8rFGi14lZGrYER6EsZVEyPXF6JAVFi+AnoEXKB/05KpCbRA21qrPeh1ijIZTDWQOnbRIzfDaXozsJm4fzaXAeas4Yj8viQ5c4YdUbILG9H1cMRR/7vvJg6ZAoGN5qftU1gorJ0aHnYsry8VZw6NpARnnCat/aiQdHL/N6CNezEWiA6/c2BHq2HRguaf7t+GyS8uE5YXlVI+OxCvM/tZQOkA+3nhtJrfoYM5GRuicmZVkacRBkYQxsVnRDE7UWxrKiMhZF1i6RzAe1Z6yyIk6Lqa9JBfrepdF6iJRXUyrg8dqXx4Os3Eyeqc3YUylc8T1RVLjQMEKetB/67HeJCxNJvtsh7W+2Bh1RhFTKL4ijxgXjanEyITFNE48kvrRdAT5Cbf40MgQB9WMWiL0Yw/Qgeu/595pRAd4tZ7kSxEqWjsfRtDR+EUf6lM86YDsxShPtluSpUGiB3uoJH3Dnbb0NdvKuOCB9oaHA/aVTEt0t0wi0wAVaA7vHeR44+WwM26G0vEWQuZJyMBmp93S0EWlqS+sDJMOSge1t2p9o8Dopx/LrnKQgbsBtNnh+4GMxq+6r7cbkuiom2hUG5QHcq62w0pT/seqGnCYj2SvUV/W3okmSoyyHfa1wIdTXzhTXGQiex79D9YVRtD4dUgWO4IO9sDqfpmUjtcDJzhUIKbUhGF0MIs8yoZ9nu7BbJed+mKKNaa4PaQrzOS5TV+a4kHHtIgm3Gideys6N8M0JWnhudN6DNBxIopbkVN/73rB+jI4cM7kPxRPhmkKatS0EaenDaXjgh/W1TEM7A8o69hm+QCepOlse0n272o54cRN3Z8sywxT/MgPxKeQI80map5LCiaHIIllfDiVIXSc+1pSINx6wNd3+2+NxfBe0ZQzjxugQ+KMU8/nc6FQbDkKG2jH2jRFBsdzvyb8v2WIcFQLO4Pq6ZKvIrqbDvF1H5Ox0Ma3h7jI5SwCDdBB0ds+3GwbMqQnHwfrXhDgZ73dbOOlTytq4V7FdXgNuz/5GQ1bfPfOTKxyb2pqytobmfo0mLgM0KHRez7cbB8jIB9cn4NBe5pXesch+uVY70yZmgJCHIP6iZtINDAd091Ww1jl26mpNh2S/mDwDIv+uIMK07WxjhVjClq9P91HrU2vhm0++4vnAXIedLgJyUy2cxTjot3ObktGhw5KSs0NWNNBOrKkQ4m8ITFUeK8vHEPRLS/pyJ74icwddAAhSh8hbKY+WdSBy87WzqAeGW06KH3wnPHBHXF7fqOCLpgi8FHu0tEi0mGK2ZNxP7n90N/0H8LKjmhFH4LLn1i8TXJqykEHtTZQQh6wHcy78WYQUCgkpnthOd0greQa4rnkI4cl0jE19W1PYxR/S9Vk+VA6RqON/7XokJYGDvtMDmiHJo0tHRITme1mbRwi9fPzUd/RBoEOmMfY5Cx0oSj9ojE19dymgxpYu44LV/CW4+KLxpAWUsS3TvWx2eino19AJkXscEA0gI7OcWF6v7YIHoeIjQFGimwOyerFul4Yy6e46QABUX4bIcq9KSc6J5gs9R+s7XWm2hiQ7CMGiVxwSKyHwQONf0qq4+G/PfwNfMQOv3GxMdU5UjC1frV0AOR/vWwQt9CW+b1iYaITY12P747K/JJRcYtGHx1LfYcUCFf0Emw54nGi6U644HFc7bh0gM8dX2MyoRhBT2w62n9owHYEnl3N8fqSfpJ1xhxc2XifkHyVk/zQMQkhMYc/cdOxNNfvaIUregs2I2unWUcjA2+8KI6RtI2mY1xCIHH1ImPqG1uFF+4NVIDiSdKBexNApgr/2h7UF+MFpLCTvjjYcxgbFX8ljxjYDIIF7eDbBRl7gbWVgRzuyujACd1ptG9BqmzU/FcL/NOBR3I4UkTgAmeg4aKDwiq+4XjlcfXKXkXJFCJMtLsghYxN1/62K6IDROTeYcj7LF/4zeEwwbBgvxt+6VN+IKMVlq+MDpmRCuHO0Uko+GtkeMfCb6HDml7Qms4Bx5mQdR6Ddexx6HhjuFzY+F87v8cHFAhCsv0OC++jfidDod1uaRrEs0/HgI8RYSm5t3FYqVQUAPxzuLFxzw8VXTp03DAnxNc7aZwQv3eV7zliZF3bxvV18dff+rpgn6OaGA/wH8F+RYgf/d+q2j5E/Wqi0g4g4iqcZs0gejF24cSJ35sOWZJxgK7iI8MWNjrLcdWrfumTpDUb6P04RWIyfm86KIuOOcE6frHTZKo+v2o6mIK2eBBhvmA6LJ/zrW7RIQiBfEVvLz8JVpvtlbDQBfgXXXOexToBvvlmlKucFM8xI99ay2sPVAGf7KvnrFfQ4a+/1DfGzx39TmwAzZ/mkqtLIB0QhKm44IMrYlhdXOdSfjmIC0J17tOULSNDBcWPFH3TZgJTURXicXvg+mpyPa1TUsTO8fMrX+7rJq0MIh5Irsx9eu5jxr/pjNhbJoCJlWogrlpGon1gmm6F6qk5q6fyCxYO+8xBQYCZjOeF6src0afnz61x9wPG+fzT0REMcwWuOPo05boCXwOXwBXJgIqPQLVe2hkXBoJP1uq4jV9RreN3gR0lWptMAu13mUMwjYfdwQoMER/UosIvkzjYBkMAV1R719hX4Lf6WB/We9FPfrlvtU1aOrKDUuIbSL4QBLwQ72AgEe0ejgbzHO8hT3qDEVzUf9SzzqrxL1xVvOjAB220IfRmOyCs9Ff48p2LvF4CPvgagZRVD7uatyr+bsiPfFFi//iW/b8OHl8e76UmUuQOPgroN70z7xrg+yrK8TIAAAHcSURBVPXuFp6NR4fQ51HXVvIgLs9TX2j81UaV+LYMD6jPyCc6e6G/QNxU42ryit5P+/vhk+/3u2MH9OiZn5eydtk76u3ToNaeL69SX7IVtXBvnPHF1z+NRce9hR4d+tLSDXiV8/EY0gGGkLSVy5u9/sT1y7YZHaw5G4KHIX9/9CtZ+yCsee5v+1KxtDyOdKx6nKtIxnLqhshED0vjzLd6bwxTI8TXb4CxcIC028RzgOrGhurbL7tft3ET0PQfdwjq8cao11v3X34FHU/XDuKucC86Hhy7tqZ44+oWHq8Rrvb5IXQEmk3/qqXeQNNBURH/1lEQNOoPbjoo6oHv+Y4LqZTgP2xr3jQvayFFfkMoCdVUquqbjpUvPHn1wMK6b2+xvJSa80sHmI4bSYfu23nGj1KpI5/MBdTDG2k6IPIgnuBNnvAF3ymt6xVwNwVLfktc6uqCe9Oj17Vf8vLBUCz4zcvUpwsLpPMWiNdeaUPLdULP+aVjQ/draAT1JkboGLK0tOLPeKjHun7sj4781fXCXTfw1pu8n0EKTZ3K+ctZrr6h5doga8eqr2giqUmU5FOQHny5q/Qj4S/WFPD+xpTHO5scuJHZbAdL6+RXyzjowPZgadlPEqfev5m68v8O9vzdVWa00QAAAABJRU5ErkJggg==',use_column_width=True)
        selected_langague = st.selectbox('Langague',['한국어','English'])
        menu = option_menu('Menu',['Home','EDA','ML'], icons = ['house-door-fill','bar-chart-line-fill','gear-wide-connected'],menu_icon="caret-down-fill", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "#243746", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#ef494c"},})

    if selected_langague == '한국어':
        st.title('생활패턴으로 알아보는 비만정도 예측 앱')
        if menu == 'Home':
            run_home()
        elif menu == 'EDA':
            run_eda()
        elif menu == 'ML':
            run_ml()
    
    elif selected_langague == 'English':
        st.title('Predict obesity level by life style')
        if menu == 'Home':
            run_home_eng()
        elif menu == 'EDA':
            run_eda_eng()
        elif menu == 'ML':
            run_ml_eng()


if __name__ == '__main__':
    main()

