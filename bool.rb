
puts("HELLO, it's test in git hash for vim and git branch ~ checkout")
<<<<<<< HEAD
puts("Branch check independence!")
puts("What ur name")
=======
puts("change in hot fix")
puts("What is ur name?")
>>>>>>> hotfix
in_name = gets.chomp();
puts("Put ur password!")
in_str = gets.chomp();

if in_str=="1234"
	puts("Welcome! : "+in_name)
	puts("what u press password : "+in_str)
elsif in_str=="11"
	puts("Welcome! : "+in_name)
	puts("what u press password : "+in_str)
else
	puts("what the fuxk, who u r?")
	puts("I dont know ["+in_name+"] is who are!")
end
