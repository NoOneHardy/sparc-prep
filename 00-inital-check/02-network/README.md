# Subnetting

This task uses the following IPv4 address:

```text
192.168.50.77/26
```

## Tasks

### Subnet mask in decimal form:

```text
CIDR: /26

1111 1111.1111 1111.1111 1111.1100 0000
255      .255      .255      .192
255.255.255.192
```

### Network address

```text
26 → 6 host bits 
2⁶ = 64

host address: 77
77 >= 64 * 1 → not in subnet 1
77 < 64 * 2 → in subnet 2
      ⤷----⤵
192.168.50.64/26
```

### Broadcast address

```text
192.168.50.127
```

### First usable host

```text
192.168.50.65
```

### Last usable host

```text
192.168.50.126
```

### Number of usable hosts

```text
127 - 65 = 62
```

## Verification

```bash
ipcalc 192.168.50.77/26
```
