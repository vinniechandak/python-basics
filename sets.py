# This file gives introduction about sets and frozensets
a = set();
a.add('aa');
a.add('bb');
a.add('cc');
a.add('aa'); # set can't contain duplicate elements
print a;

b = set(['11','12','13','aa','dd']);
print b;

c = a.union(b);
print 'Union:', c;
d = a.intersection(b);
print 'Intersection:', d;
e = a.difference(b);
print 'Difference:', e;

# frozenset are immutable sets.

p = frozenset(['aa','bb','cc']);
#p.add('dd'); # this won't work as frozenset are immutable and doesn't provide add method as API.
print p;