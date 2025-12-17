#!/bin/bash
MODULE="build/Release/audify.node"

echo "=== Symboles non résolus par aucune bibliothèque visible ==="

# Symboles non définis du module (strip les versions @XXX)
nm -u "$MODULE" | awk '{print $2}' | sed 's/@.*//' | sort -u > /tmp/undef.txt

# Symboles fournis par toutes les dépendances (tous types sauf undefined)
{
    for lib in $(ldd "$MODULE" | grep "=>" | awk '{print $3}'); do
        if [ -f "$lib" ]; then
            # On prend TOUS les symboles définis (pas seulement T)
            nm -D "$lib" 2>/dev/null | grep -v " U " | awk 'NF>=3 {print $3}' | sed 's/@.*//'
        fi
    done
    # Inclure aussi les symboles de Node.js
    nm -D $(which node) 2>/dev/null | grep -v " U " | awk 'NF>=3 {print $3}' | sed 's/@.*//'
} | sort -u > /tmp/defined.txt

# Différence = symboles vraiment orphelins
comm -23 /tmp/undef.txt /tmp/defined.txt | c++filt

echo -e "\n=== Nombre de symboles orphelins ==="
comm -23 /tmp/undef.txt /tmp/defined.txt | wc -l