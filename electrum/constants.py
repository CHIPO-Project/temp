# -*- coding: utf-8 -*-
#
# Electrum - lightweight Chipo client
# Copyright (C) 2018 The Electrum developers
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import json

from .util import inv_dict


def read_json(filename, default):
    path = os.path.join(os.path.dirname(__file__), filename)
    try:
        with open(path, 'r') as f:
            r = json.loads(f.read())
    except:
        r = default
    return r


GIT_REPO_URL = "https://github.com/spesmilo/electrum"
GIT_REPO_ISSUES_URL = "https://github.com/spesmilo/electrum/issues"


class AbstractNet:

    @classmethod
    def max_checkpoint(cls) -> int:
        return max(0, len(cls.CHECKPOINTS) * 2016 - 1)


class BitcoinMainnet(AbstractNet):

    TESTNET = False
    WIF_PREFIX = 156
    ADDRTYPE_P2PKH = 28
    ADDRTYPE_P2SH = 13
    SEGWIT_HRP = ""
    GENESIS = "00000d6a63eb633e56ce5f7b1bd3a0f2126e500d2bd65affda33c775920acb88"
    DEFAULT_PORTS = {'t': '50001', 's': '50002'}
    DEFAULT_SERVERS = read_json('servers.json', {})
    CHECKPOINTS = read_json('checkpoints.json', [])

    XPRV_HEADERS = {
        'standard':    0x041F8F61,
        #'p2wpkh-p2sh': 0x049d7878,  # yprv
        #'p2wsh-p2sh':  0x0295b005,  # Yprv
        #'p2wpkh':      0x04b2430c,  # zprv
        #'p2wsh':       0x02aa7a99,  # Zprv
    }
    XPRV_HEADERS_INV = inv_dict(XPRV_HEADERS)
    XPUB_HEADERS = {
        'standard':    0x03E12FA5,
        #'p2wpkh-p2sh': 0x049d7cb2,  # ypub
        #'p2wsh-p2sh':  0x0295b43f,  # Ypub
        #'p2wpkh':      0x04b24746,  # zpub
        #'p2wsh':       0x02aa7ed3,  # Zpub
    }
    XPUB_HEADERS_INV = inv_dict(XPUB_HEADERS)
    BIP44_COIN_TYPE = 437


class BitcoinTestnet(AbstractNet):

    TESTNET = True
    WIF_PREFIX = 194
    ADDRTYPE_P2PKH = 66
    ADDRTYPE_P2SH = 3
    SEGWIT_HRP = ""
    GENESIS = "000003bdafaf3aa717d2ffe487af95ce6c92204eadbb6385d02aae69254ded67"
    DEFAULT_PORTS = {'t': '51001', 's': '51002'}
    DEFAULT_SERVERS = read_json('servers_testnet.json', {})
    CHECKPOINTS = read_json('checkpoints_testnet.json', [])

    XPRV_HEADERS = {
        'standard':    0x042211C2,
        #'p2wpkh-p2sh': 0x044a4e28,  # uprv
        #'p2wsh-p2sh':  0x024285b5,  # Uprv
        #'p2wpkh':      0x045f18bc,  # vprv
        #'p2wsh':       0x02575048,  # Vprv
    }
    XPRV_HEADERS_INV = inv_dict(XPRV_HEADERS)
    XPUB_HEADERS = {
        'standard':    0x03E3B206,
        #'p2wpkh-p2sh': 0x044a5262,  # upub
        #'p2wsh-p2sh':  0x024289ef,  # Upub
        #'p2wpkh':      0x045f1cf6,  # vpub
        #'p2wsh':       0x02575483,  # Vpub
    }
    XPUB_HEADERS_INV = inv_dict(XPUB_HEADERS)
    BIP44_COIN_TYPE = 1


class BitcoinRegtest(BitcoinTestnet):

    SEGWIT_HRP = ""
    GENESIS = "00000bfd7b376c469fd66c0121df4f9b368a46a9afe3f685fa0454bbc521e090"
    DEFAULT_SERVERS = read_json('servers_regtest.json', {})
    CHECKPOINTS = []


class BitcoinSimnet(BitcoinTestnet):

    SEGWIT_HRP = ""
    GENESIS = ""
    DEFAULT_SERVERS = read_json('servers_regtest.json', {})
    CHECKPOINTS = []


# don't import net directly, import the module instead (so that net is singleton)
net = BitcoinMainnet

def set_simnet():
    global net
    net = BitcoinSimnet

def set_mainnet():
    global net
    net = BitcoinMainnet


def set_testnet():
    global net
    net = BitcoinTestnet


def set_regtest():
    global net
    net = BitcoinRegtest
