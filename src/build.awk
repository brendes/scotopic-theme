FILENAME != template {
	if (NF >= 2 && !/^#/) {
		k = $1
		val = $0; sub(/^[^ \t]+[ \t]+/, "", val)
		v[k] = val
	}
	next
}

!resolved {
	do {
		changed = 0
		for (k in v)
			for (j in v)
				if (v[k] ~ "[{]" j "[}]") {
					gsub("[{]" j "[}]", v[j], v[k])
					changed = 1
				}
	} while (changed)
	resolved = 1
}

{
	for (k in v)
		gsub("[{]" k "[}]", v[k])
	print
}

