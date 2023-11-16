# Increase file descriptor limit

exec { 'change-os-configuration-for-holberton-user':
  command => '/bin/sed -i "s/nofile 5/nofile 40000/" /etc/security/limits.conf',
  notify  => Exec['replace'],
}

exec { 'replace':
  command => '/bin/sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
