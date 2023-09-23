# This manifest kills a process named killmenow

exec { 'Kill_killmenow':
  command => '/usr/bin/pkill -f killmenow'
}
