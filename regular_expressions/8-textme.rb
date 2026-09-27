#!/usr/bin/env ruby
line = ARGV[0]
sender = line.match(/\[from:(.*?)\]/)[1]
receiver = line.match(/\[to:(.*?)\]/)[1]
flags = line.match(/\[flags:(.*?)\]/)[1]
puts "#{sender},#{receiver},#{flags}"
