#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k8.py

if __name__ == '__main__':
    def cipher(msg: str):
        msg_list = [chr(219 - ord(i)) if i.isalpha and i.islower() else i for i in list(msg)]
        return "".join(msg_list)

    print(cipher("I couldn't believe that I could actually understand what I was reading :"
                 " the phenomenal power of the human mind ."))

    print(cipher("I xlfowm'g yvorvev gszg I xlfow zxgfzoob fmwvihgzmw dszg I dzh ivzwrmt :"
                 " gsv ksvmlnvmzo kldvi lu gsv sfnzm nrmw ."))
