#!/bin/bash
find . -name '*.mo' -delete
mkdir -p unicorecmscrea/locale

pot-create -o unicorecmscrea/locale/unicorecmscrea.pot unicorecmscrea/

declare -a arr=("eng_GB" "spa_ES")

for lang in "${arr[@]}"
do
    mkdir -p "unicorecmscrea/locale/""$lang""/LC_MESSAGES"

    if [ ! -f "unicorecmscrea/locale/""$lang""/LC_MESSAGES/unicorecmscrea.po" ]; then
        msginit -l $lang -i unicorecmscrea/locale/unicorecmscrea.pot -o unicorecmscrea/locale/$lang/LC_MESSAGES/unicorecmscrea.po
    fi

    msgmerge --update unicorecmscrea/locale/$lang/LC_MESSAGES/unicorecmscrea.po unicorecmscrea/locale/unicorecmscrea.pot
    msgfmt unicorecmscrea/locale/$lang/LC_MESSAGES/*.po -o unicorecmscrea/locale/$lang/LC_MESSAGES/unicorecmscrea.mo
done
