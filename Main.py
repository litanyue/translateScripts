import argparse
from typing import Iterator, NoReturn

from polyglot.detect import Detector
from polyglot.detect.base import UnknownLanguage

import CaiYun
import Google


def main(text: str, translator) -> NoReturn:
	"""
	print the translation to the stdout
	:param translator: a class which to call translate function and get the result
	:param text: source text
	:return: none
	"""
	paragraphs: Iterator[str] = filter(lambda x: x, text.split('\n'))
	for paragraph in paragraphs:
		try:
			detector = Detector(paragraph)
		except UnknownLanguage:
			print("无法检测源语言")
		else:
			language: str = detector.language.code
			print(paragraph)
			print(translator.translate([paragraph], language))
			print(u"Detected source language: {}".format(detector.language.name))


if __name__ == '__main__':
	translators = {"CaiYun": CaiYun.CaiYun(), "Google": Google.Google()}
	parser = argparse.ArgumentParser(description="use translators to translate text")
	parser.add_argument("text", type=str, help="the source text you want to translate")
	parser.add_argument("-t", "--translator", type=str, default="Google",
	                    choices=translators.keys(),
	                    help="specify the translator you want to use (default: %(default)s)")
	args = parser.parse_args()
	text = args.text.replace('\n', ' ')
	main(text, translators.get(args.translator))
