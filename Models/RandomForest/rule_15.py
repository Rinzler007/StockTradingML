def findDecision(obj):
   # Feature: RSI, Instances: 115, Entropy: 0.9842
   if obj[1] == 'Hold':
      # Feature: BB, Instances: 93, Entropy: 0.9758
      if obj[3] == 'Sell':
         # Feature: Closing, Instances: 63, Entropy: 0.9984
         if obj[0]>38.720001:
            # Feature: MACD, Instances: 42, Entropy: 0.9403
            if obj[2] == 'Sell':
               # Feature: SMA1, Instances: 28, Entropy: 0.8631
               if obj[4] == 'Buy':
                  # Feature: SMA2, Instances: 22, Entropy: 0.9457
                  if obj[5] == 'Buy':
                     return 'No'
                  elif obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Sell':
                  return 'No'
               else:
                  return 'No'
            elif obj[2] == 'Buy':
               # Feature: SMA1, Instances: 14, Entropy: 1.0
               if obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 11, Entropy: 0.994
                  if obj[5] == 'Sell':
                     return 'Yes'
                  elif obj[5] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Buy':
                  # Feature: SMA2, Instances: 3, Entropy: 0.9183
                  if obj[5] == 'Sell':
                     return 'No'
                  elif obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'No'
         elif obj[0]<=38.720001:
            # Feature: MACD, Instances: 21, Entropy: 0.8631
            if obj[2] == 'Sell':
               # Feature: SMA1, Instances: 13, Entropy: 0.6194
               if obj[4] == 'Buy':
                  # Feature: SMA2, Instances: 9, Entropy: 0.7642
                  if obj[5] == 'Buy':
                     return 'Yes'
                  elif obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[2] == 'Buy':
               # Feature: SMA1, Instances: 8, Entropy: 1.0
               if obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 7, Entropy: 0.9852
                  if obj[5] == 'Sell':
                     return 'No'
                  elif obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[4] == 'Buy':
                  return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'Yes'
      elif obj[3] == 'Hold':
         # Feature: Closing, Instances: 27, Entropy: 0.6052
         if obj[0]>38.720001:
            # Feature: SMA1, Instances: 15, Entropy: 0.8366
            if obj[4] == 'Buy':
               # Feature: MACD, Instances: 11, Entropy: 0.684
               if obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 7, Entropy: 0.5917
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  # Feature: SMA2, Instances: 4, Entropy: 0.8113
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[4] == 'Sell':
               # Feature: SMA2, Instances: 4, Entropy: 1.0
               if obj[5] == 'Buy':
                  # Feature: MACD, Instances: 3, Entropy: 0.9183
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
         elif obj[0]<=38.720001:
            return 'Yes'
         else:
            return 'Yes'
      elif obj[3] == 'Buy':
         # Feature: MACD, Instances: 3, Entropy: 0.9183
         if obj[2] == 'Buy':
            # Feature: Closing, Instances: 2, Entropy: 1.0
            if obj[0]<=38.720001:
               # Feature: SMA1, Instances: 2, Entropy: 1.0
               if obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 2, Entropy: 1.0
                  if obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[2] == 'Sell':
            return 'Yes'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[1] == 'Sell':
      # Feature: SMA1, Instances: 13, Entropy: 0.6194
      if obj[4] == 'Buy':
         return 'Yes'
      elif obj[4] == 'Sell':
         # Feature: Closing, Instances: 3, Entropy: 0.9183
         if obj[0]>38.720001:
            return 'No'
         elif obj[0]<=38.720001:
            return 'Yes'
         else:
            return 'Yes'
      else:
         return 'No'
   elif obj[1] == 'Buy':
      return 'No'
   else:
      return 'No'
