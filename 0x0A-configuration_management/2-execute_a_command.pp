# exec resource to kill a process named killmenow
exec { 'kill killmenow':
  command => '/usr/bin/pkill -f killmenow'
}
