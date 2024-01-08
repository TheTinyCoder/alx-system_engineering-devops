#!/usr/bin/env ruby
puts ARGV[0].scan(/(\[from:|\[to:|\[flags:)(.*?)(\])/).map{|ar| ar[1]}.join(",")
