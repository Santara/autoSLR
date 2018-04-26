find /home/ashutosh/Sudeshna/ARTICLES/all_papers/ -type f -print0 | \
perl -n0e '$new = $_; if($new =~ s/[^[:ascii:]]/_/g) {
  print("Renaming $_ to $new\n"); rename($_, $new);
}'