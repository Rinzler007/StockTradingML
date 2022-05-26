def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9995
   if obj[3] == 'Sell':
      # Feature: Closing, Instances: 79, Entropy: 0.9484
      if obj[0]>38.068001:
         # Feature: MACD, Instances: 58, Entropy: 0.8727
         if obj[2] == 'Sell':
            # Feature: RSI, Instances: 41, Entropy: 0.9474
            if obj[1] == 'Hold':
               # Feature: SMA1, Instances: 39, Entropy: 0.9612
               if obj[4] == 'Buy':
                  # Feature: SMA2, Instances: 33, Entropy: 0.9457
                  if obj[5] == 'Buy':
                     return 'No'
                  elif obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 6, Entropy: 1.0
                  if obj[5] == 'Sell':
                     return 'No'
                  elif obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'No'
            elif obj[1] == 'Buy':
               return 'No'
            else:
               return 'No'
         elif obj[2] == 'Buy':
            # Feature: SMA2, Instances: 17, Entropy: 0.5226
            if obj[5] == 'Sell':
               # Feature: SMA1, Instances: 16, Entropy: 0.3373
               if obj[4] == 'Sell':
                  # Feature: RSI, Instances: 14, Entropy: 0.3712
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Buy':
                  return 'No'
               else:
                  return 'No'
            elif obj[5] == 'Buy':
               return 'Yes'
            else:
               return 'Yes'
         else:
            return 'No'
      elif obj[0]<=38.068001:
         # Feature: RSI, Instances: 21, Entropy: 0.9852
         if obj[1] == 'Hold':
            # Feature: SMA2, Instances: 19, Entropy: 0.9819
            if obj[5] == 'Buy':
               # Feature: MACD, Instances: 10, Entropy: 0.8813
               if obj[2] == 'Sell':
                  # Feature: SMA1, Instances: 9, Entropy: 0.9183
                  if obj[4] == 'Buy':
                     return 'Yes'
                  elif obj[4] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Buy':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Sell':
               # Feature: MACD, Instances: 9, Entropy: 0.9911
               if obj[2] == 'Buy':
                  # Feature: SMA1, Instances: 6, Entropy: 0.9183
                  if obj[4] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[1] == 'Sell':
            return 'Yes'
         elif obj[1] == 'Buy':
            return 'No'
         else:
            return 'No'
      else:
         return 'Yes'
   elif obj[3] == 'Hold':
      # Feature: Closing, Instances: 32, Entropy: 0.6253
      if obj[0]>38.068001:
         # Feature: RSI, Instances: 21, Entropy: 0.7919
         if obj[1] == 'Hold':
            # Feature: SMA1, Instances: 13, Entropy: 0.9612
            if obj[4] == 'Buy':
               # Feature: MACD, Instances: 8, Entropy: 0.8113
               if obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 6, Entropy: 0.65
                  if obj[5] == 'Sell':
                     return 'Yes'
                  elif obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  # Feature: SMA2, Instances: 2, Entropy: 1.0
                  if obj[5] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Sell':
               # Feature: SMA2, Instances: 5, Entropy: 0.971
               if obj[5] == 'Buy':
                  # Feature: MACD, Instances: 4, Entropy: 0.8113
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'No'
         elif obj[1] == 'Sell':
            return 'Yes'
         else:
            return 'Yes'
      elif obj[0]<=38.068001:
         return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      return 'No'
   else:
      return 'No'
