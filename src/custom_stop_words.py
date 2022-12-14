
other_stop_words = ['junior', 'senior', 'experience', 'etc', 'job', 'work', 'company', 'technique',
                    'candidate', 'skill', 'skills', 'language', 'menu', 'inc', 'new', 'plus', 'years',
                    'technology', 'organization', 'ceo', 'cto', 'account', 'manager', 'data', 'scientist', 'mobile',
                    'developer', 'product', 'revenue', 'strong', 'people', 'business', 'solution', 'working',
                    'customer', 'knowledge', 'help', 'client', 'help', 'looking', 'offer', 'part', 'value',
                    'management', 'engineer', 'engineering', 'well', 'opportunity', 'team', 'development', 'software',
                    'application', 'good', 'improve', 'build', 'want', 'career', 'one', 'big', 'able', 'based',
                    'requirement', 'focus', 'understanding', 'learn', 'use', 'time', 'employee', 'best', 'innovative',
                    'tool', 'design', 'platform', 'system', 'environment', 'project', 'service', 'colleague', 'provide',
                    'technical', 'process', 'support', 'world', 'deliver', 'join', 'create', 'role', 'process',
                    'developing', 'remote', 'together', 'information', 'computer', 'develop', 'analytic', 'including',
                    'make', 'member', 'industry', 'architecture', 'within', 'using', 'take', 'code', 'make', 'first',
                    'expert', 'way', 'across', 'using', 'ensure', 'belgium', 'great', 'challenge', 'professional',
                    'need', 'day', 'different', 'challenge', 'expertise', 'agile', 'mission', 'practice', 'ability',
                    'user', 'responsible', 'enable', 'culture', 'year', 'grow', 'u', 'apply', 'international',
                    'partner', 'share', 'understand', 'responsibility', 'required', 'open', 'existing', 'market',
                    'area', 'various', 'right', 'used', 'internal', 'lead', 'end', 'existing', 'building', 'every',
                    'related', 'know', 'key', 'testing', 'group', 'source', 'leading', 'implement', 'communication',
                    'training', 'digital', 'growth', 'related', 'group', 'bring', 'advanced', 'least', 'programming',
                    'excellent', 'participate', 'future', 'personal', 'passionate', 'quality', 'stakeholder',
                    'passion', 'approach', 'task', 'multiple', 'warehouse', 'driven', 'diverse', 'relevant',
                    'country', 'strategy', 'position', 'diverse', 'drive', 'around', 'impact', 'making', 'around',
                    'complex', 'integration', 'gone', 'eg', 'algorithm', 'strategy', 'idea', 'insight', 'infrastructure',
                    'dynamic', 'high', 'include', 'level', 'security', 'science', 'test', 'growing', 'large', 'global',
                    'flexible', 'brussel', 'individual', 'leader', 'challenging', 'large', 'game', 'start', 'production'
                    , 'become', 'writing', 'collaborate', 'field', 'ai', 'analytics', 'available', 'performance',
                    'innovation', 'problem', 'implementation', 'real', 'must', 'contribute', 'better',
                    'brussels', 'set', 'reporting', 'tribute', 'interest', 'office', 'closely', 'life', 'hour', 'fast',
                    'creating', 'hand', 'providing', 'ownership', 'success', 'tech', 'scale', 'modern', 'place',
                    'problem', 'creating', 'exciting', 'community', 'benefit', 'workshop', 'standard', 'smart',
                    'degree', 'analytical', 'analysis', 'location', 'concept', 'location', 'range', 'following',
                    'strong', 'please', 'recruitment', 'delivery', 'experienced', 'sharing', 'always', 'master',
                    'unique', 'currently', 'space', 'change', 'solving', 'currently', 'activity', 'similar', 'change',
                    'maintain', 'designing', 'others', 'highly', 'believe', 'review', 'interested', 'player', 'feature',
                    'deployment', 'intelligence', 'many', 'financial', 'improvement', 'fully', 'care', 'decision',
                    'specific', 'initiative', 'come', 'implementing', 'energy', 'solve', 'profile', 'solid', 'asset',
                    'additional', 'operating', 'operation', 'control', 'built', 'processing', 'scalable', 'complete',
                    'electronic', 'top', 'critical', 'continuous', 'europe', 'expect', 'give', 'automation', 'model',
                    'embedded', 'framework', 'program', 'vision', 'stack', 'full', 'backend',
                    'database', 'distributed', 'web', 'deep', 'hardware', 'background', 'core', 'microsoft',
                    'functional', 'considered', 'fluent', 'dutch', 'french', 'written', 'preferably',
                    'successful', 'ml', 'order', 'course', 'meet', 'identify', 'methodology', 'presentation',
                    'proven', 'mindset', 'deploying', 'factory', 'familiarity', 'bachelor', 'minimum', 'electronics'
                    , 'e', 'g', 'pipeline', 'current', 'english', 'familiar', 'relational', 'principle', 'storage',
                    'effectively', 'mathematics', 'clean', 'willing', 'statistic', 'practical', 'modelling',
                    'server', 'modeling', 'scripting', 'independently', 'optimization', 'protocol', 'maintaining',
                    'basic', 'non', 'nice', 'coding', 'equivalent', 'comfortable', 'applied', 'package', 'automated',
                    'manage', 'enjoy', 'bonus', 'qualification', 'either', 'cross', 'verbal', 'managing', 'common',
                    'welcome', 'write', 'oriented', 'networking', 'library', 'window', 'industrial', 'fundamental',
                    'phd', 'latest', 'computing', 'paced', 'external', 'integrate', 'app', 'european', 'eager',
                    'improving', 'variety', 'running', 'debug', 'commercial', 'mandatory', 'issue', 'healthy',
                    'network', 'domain', 'proficient', 'function', 'research', 'device', 'statistical', 'ideally',
                    'supported', 'disability', 'interpersonal', 'purpose', 'consultant', 'safety', 'documentation',
                    'lake', 'speak', 'simulation', 'sound', 'topic', 'orchestration', 'preferred', 'fluency', 'tooling',
                    'architect', 'gender', 'hive', 'paid', 'proficiency', 'prior', 'unit', 'collect', 'google',
                    'inclusive', 'spoken', 'status', 'identity', 'cycle', 'front', 'machine', 'learning', 'cloud']
